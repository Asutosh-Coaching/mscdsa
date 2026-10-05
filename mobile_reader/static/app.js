/**
 * Lumina MSCDSA Mobile Study & Reader System - Application Logic
 * Mobile-First, Touch-Optimized Client Controller
 */

const AppState = {
  curriculum: null,
  stats: null,
  currentView: 'home',
  activeCourse: null,
  activeUnit: null,
  activeSemester: 'Semester_1',
  speechSynth: window.speechSynthesis,
  speechUtterance: null,
  isSpeaking: false,
  isPaused: false,
  speechRate: 1.0,
  theme: localStorage.getItem('lumina_theme') || 'sepia',
  fontSize: localStorage.getItem('lumina_font_size') || '17',
  fontFamily: localStorage.getItem('lumina_font_family') || 'sans',
  readTimerInterval: null,
  secondsReadInUnit: 0,
  noteDebounceTimer: null
};

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
  applyTheme(AppState.theme);
  applyTypography(AppState.fontSize, AppState.fontFamily);
  setupEventListeners();
  loadCurriculum();

  // Register Service Worker
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(err => console.log('SW registration error:', err));
  }
});

// --- API Calls ---
async function loadCurriculum() {
  try {
    const res = await fetch('/api/curriculum');
    const data = await res.json();
    AppState.curriculum = data.curriculum;
    AppState.stats = data.stats;

    renderStats(data.stats);
    renderResumeCard(data.last_read);
    renderCoursesList();
    renderQRInfo(data.local_network_ip);
  } catch (err) {
    console.error('Failed to load curriculum:', err);
  }
}

async function loadUnit(courseCode, unitId) {
  try {
    showLoading();
    const res = await fetch(`/api/unit/${courseCode}/${unitId}`);
    const unit = await res.json();

    AppState.activeCourse = courseCode;
    AppState.activeUnit = unitId;

    renderReader(unit);
    switchView('reader');

    // Start reading timer
    clearInterval(AppState.readTimerInterval);
    AppState.secondsReadInUnit = 0;
    AppState.readTimerInterval = setInterval(() => {
      AppState.secondsReadInUnit += 5;
      if (AppState.secondsReadInUnit % 15 === 0) {
        syncReadingProgress(false);
      }
    }, 5000);

  } catch (err) {
    alert('Failed to load unit content.');
    console.error(err);
  } finally {
    hideLoading();
  }
}

async function syncReadingProgress(isCompleted = false) {
  if (!AppState.activeCourse || !AppState.activeUnit) return;

  const scrollPercent = calculateScrollPercent();
  const status = isCompleted ? 'completed' : 'in_progress';

  try {
    const res = await fetch('/api/progress/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        course_code: AppState.activeCourse,
        unit_id: AppState.activeUnit,
        status: status,
        scroll_percent: scrollPercent,
        added_seconds: AppState.secondsReadInUnit
      })
    });
    const data = await res.json();
    AppState.stats = data.stats;
    renderStats(data.stats);
    AppState.secondsReadInUnit = 0;
  } catch (err) {
    console.warn('Progress sync error:', err);
  }
}

// --- Render Functions ---

function renderStats(stats) {
  if (!stats) return;
  document.getElementById('stat-completed').textContent = stats.completed_units || 0;
  document.getElementById('stat-streak').textContent = `${stats.study_streak_days || 1} 🔥`;
  document.getElementById('stat-time').textContent = `${Math.round(stats.total_minutes || 0)}m`;
  document.getElementById('stat-today').textContent = `${Math.round(stats.today_minutes || 0)}m`;
}

function renderResumeCard(lastRead) {
  const container = document.getElementById('resume-card-container');
  if (!lastRead) {
    container.innerHTML = `
      <div class="resume-card">
        <div class="resume-label">Welcome to MSCDSA Study System</div>
        <div class="resume-title">Start Your First Unit</div>
        <div class="resume-subtitle">Select any course from Semester 1 or Semester 2 to begin.</div>
        <button class="btn-primary" onclick="switchView('courses')">Explore Courses →</button>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="resume-card">
      <div class="resume-label">Resume Where You Left Off</div>
      <div class="resume-title">${lastRead.unit_num}: ${lastRead.unit_title}</div>
      <div class="resume-subtitle">${lastRead.course_code}: ${lastRead.course_title}</div>
      <div class="progress-track">
        <div class="progress-bar-fill" style="width: ${Math.max(5, Math.round(lastRead.scroll_percent || 0))}%"></div>
      </div>
      <div style="display:flex; gap:10px;">
        <button class="btn-primary" onclick="loadUnit('${lastRead.course_code}', '${lastRead.unit_id}')">
          Continue Reading (${Math.round(lastRead.scroll_percent || 0)}%) ▶
        </button>
      </div>
    </div>
  `;
}

function renderCoursesList() {
  const container = document.getElementById('courses-container');
  if (!AppState.curriculum) return;

  const courses = AppState.curriculum.semesters[AppState.activeSemester] || [];
  let html = '';

  courses.forEach(c => {
    const pct = c.completion_percentage || 0;
    html += `
      <div class="course-card" onclick="openCourseRoadmap('${c.code}')">
        <div class="course-header">
          <span class="course-code">${c.code}</span>
          <span class="course-badge">${c.credits} Credits • ${c.type}</span>
        </div>
        <div class="course-title">${c.title}</div>
        <div class="course-desc">${c.description}</div>
        <div class="progress-track" style="margin-bottom:8px;">
          <div class="progress-bar-fill" style="width: ${pct}%"></div>
        </div>
        <div class="course-meta-row">
          <span>${c.completed_units || 0} of ${c.total_units} Units Done</span>
          <span style="font-weight:700; color:var(--primary);">${pct}%</span>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

function openCourseRoadmap(courseCode) {
  const semCourses = AppState.curriculum.semesters[AppState.activeSemester] || [];
  const course = semCourses.find(c => c.code === courseCode);
  if (!course) return;

  AppState.activeCourse = courseCode;
  document.getElementById('roadmap-title').textContent = `${course.code}: ${course.title}`;
  document.getElementById('roadmap-solution-btn').onclick = () => loadAssignmentSolution(course.code);

  const container = document.getElementById('roadmap-units-list');
  let html = '';

  course.units.forEach(u => {
    const statusClass = u.status || 'not_started';
    const statusText = u.status === 'completed' ? '✓ Completed' : (u.status === 'in_progress' ? '● In Progress' : 'Not Started');

    html += `
      <div class="unit-list-item" onclick="loadUnit('${course.code}', '${u.unit_id}')">
        <div class="unit-item-info">
          <div class="unit-item-tag">${u.unit_num}</div>
          <div class="unit-item-title">${u.title}</div>
          <div class="unit-item-meta">
            <span>⏱ ~${u.est_read_time_minutes} min read</span>
            <span>📄 ${u.total_pages} pages</span>
            ${u.flashcards_count ? `<span>💡 ${u.flashcards_count} checkpoints</span>` : ''}
          </div>
        </div>
        <span class="status-badge ${statusClass}">${statusText}</span>
      </div>
    `;
  });

  container.innerHTML = html;
  switchView('roadmap');
}

function renderReader(unit) {
  // Update header
  document.getElementById('reader-course-label').textContent = unit.course_code;
  document.getElementById('reader-title-label').textContent = `${unit.unit_num}: ${unit.title}`;

  // Unit Hero
  document.getElementById('unit-hero-num').textContent = unit.unit_num;
  document.getElementById('unit-hero-title').textContent = unit.title;
  document.getElementById('unit-pill-time').textContent = `⏱ ~${unit.est_read_time_minutes} min read`;
  document.getElementById('unit-pill-pages').textContent = `📄 ${unit.total_pages} pages`;

  // Objectives
  const objContainer = document.getElementById('unit-objectives-box');
  if (unit.objectives && unit.objectives.length > 0) {
    objContainer.style.display = 'block';
    const list = document.getElementById('unit-objectives-list');
    list.innerHTML = unit.objectives.map(o => `<li>${o}</li>`).join('');
  } else {
    objContainer.style.display = 'none';
  }

  // HTML Content
  document.getElementById('reader-html-stream').innerHTML = unit.html_content;

  // Flashcards
  renderFlashcards(unit.flashcards);

  // Status button
  const completeBtn = document.getElementById('btn-mark-complete');
  if (unit.user_status === 'completed') {
    completeBtn.classList.add('is-completed');
    completeBtn.innerHTML = '✓ Unit Completed';
  } else {
    completeBtn.classList.remove('is-completed');
    completeBtn.innerHTML = 'Mark Unit as Completed ★';
  }

  // Navigation Prev / Next
  const navContainer = document.getElementById('reader-unit-nav');
  let navHtml = '';
  if (unit.prev_unit) {
    navHtml += `<button class="btn-primary" style="background:var(--bg-card); color:var(--text-primary); border:1px solid var(--border-color);" onclick="loadUnit('${unit.course_code}', '${unit.prev_unit.unit_id}')">← ${unit.prev_unit.unit_num}</button>`;
  } else {
    navHtml += `<div></div>`;
  }
  if (unit.next_unit) {
    navHtml += `<button class="btn-primary" onclick="loadUnit('${unit.course_code}', '${unit.next_unit.unit_id}')">Next: ${unit.next_unit.unit_num} →</button>`;
  }
  navContainer.innerHTML = navHtml;

  // User Notes
  document.getElementById('unit-notes-input').value = unit.user_note || '';

  // Setup PDF button
  document.getElementById('reader-pdf-toggle').onclick = () => togglePdfView(unit.relative_pdf_path);

  // Scroll to previous position
  window.scrollTo(0, 0);
  if (unit.user_scroll_percent && unit.user_scroll_percent > 5) {
    setTimeout(() => {
      const targetScroll = (document.documentElement.scrollHeight - window.innerHeight) * (unit.user_scroll_percent / 100);
      window.scrollTo({ top: targetScroll, behavior: 'smooth' });
    }, 300);
  }
}

function renderFlashcards(flashcards) {
  const container = document.getElementById('flashcards-container');
  if (!flashcards || flashcards.length === 0) {
    container.innerHTML = '<p class="reader-p" style="color:var(--text-muted);">No self-assessment checkpoints for this module.</p>';
    return;
  }

  let html = '';
  flashcards.forEach((fc, idx) => {
    html += `
      <div class="flashcard" onclick="this.classList.toggle('flipped')">
        <div class="flashcard-inner">
          <div class="flashcard-front">
            <div class="card-tag">Checkpoint #${idx + 1} • Tap to Reveal</div>
            <div class="card-text">${fc.question}</div>
          </div>
          <div class="flashcard-back">
            <div class="card-tag" style="color:#fff;">Explanation / Answer</div>
            <div class="card-text">${fc.hint}</div>
            <div class="card-hint">Tap again to flip back</div>
          </div>
        </div>
      </div>
    `;
  });
  container.innerHTML = html;
}

async function loadAssignmentSolution(courseCode) {
  try {
    showLoading();
    const res = await fetch(`/api/solution/${courseCode}`);
    const data = await res.json();

    document.getElementById('solution-title').textContent = `${courseCode} Assignment Solutions`;
    // Render clean pre-formatted markdown
    document.getElementById('solution-content').innerHTML = `
      <div style="background:var(--bg-card); padding:16px; border-radius:var(--radius-md); border:1px solid var(--border-color); font-family:var(--font-mono); font-size:13px; white-space:pre-wrap; overflow-x:auto;">${escapeHtml(data.markdown_content)}</div>
    `;
    switchView('solutions');
  } catch (err) {
    alert('Assignment solution file not found for this course.');
  } finally {
    hideLoading();
  }
}

function renderQRInfo(ip) {
  const el = document.getElementById('qr-ip-display');
  if (el) {
    el.innerHTML = `<strong>Mobile Access:</strong> Open <code>http://${ip}:8000</code> in your phone's browser on the same Wi-Fi.`;
  }
}

// --- Text-to-Speech (Audio Mode) ---
function toggleAudioMode() {
  if (!AppState.speechSynth) {
    alert('Text-to-speech is not supported on this browser.');
    return;
  }

  const audioBar = document.getElementById('audio-player-bar');

  if (AppState.isSpeaking) {
    if (AppState.isPaused) {
      AppState.speechSynth.resume();
      AppState.isPaused = false;
      document.getElementById('btn-audio-play').textContent = '⏸';
    } else {
      AppState.speechSynth.pause();
      AppState.isPaused = true;
      document.getElementById('btn-audio-play').textContent = '▶';
    }
    return;
  }

  // Extract clean text to speak
  const textElements = document.querySelectorAll('#reader-html-stream p.reader-p, #reader-html-stream h3');
  let fullText = Array.from(textElements).map(el => el.textContent).join('. ');
  if (!fullText.trim()) return;

  // Truncate to first 5000 chars for speech queue chunking
  const utterance = new SpeechSynthesisUtterance(fullText.slice(0, 8000));
  utterance.rate = AppState.speechRate;
  utterance.pitch = 1.0;

  utterance.onend = () => {
    AppState.isSpeaking = false;
    AppState.isPaused = false;
    audioBar.classList.remove('active');
  };

  utterance.onerror = (e) => {
    console.error('Speech error:', e);
    AppState.isSpeaking = false;
    audioBar.classList.remove('active');
  };

  AppState.speechSynth.cancel(); // Cancel any existing
  AppState.speechSynth.speak(utterance);
  AppState.speechUtterance = utterance;
  AppState.isSpeaking = true;
  AppState.isPaused = false;

  audioBar.classList.add('active');
  document.getElementById('btn-audio-play').textContent = '⏸';
}

function stopAudio() {
  if (AppState.speechSynth) {
    AppState.speechSynth.cancel();
  }
  AppState.isSpeaking = false;
  AppState.isPaused = false;
  document.getElementById('audio-player-bar').classList.remove('active');
}

function changeAudioSpeed(newRate) {
  AppState.speechRate = parseFloat(newRate);
  if (AppState.isSpeaking) {
    stopAudio();
    toggleAudioMode();
  }
}

// --- Event Handlers & View Switching ---

function setupEventListeners() {
  // Navigation tabs
  document.querySelectorAll('.bottom-nav .nav-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const view = btn.dataset.view;
      if (view) switchView(view);
    });
  });

  // Semester switcher tabs
  document.querySelectorAll('.tab-btn[data-sem]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn[data-sem]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      AppState.activeSemester = btn.dataset.sem;
      renderCoursesList();
    });
  });

  // Scroll listener for progress line
  window.addEventListener('scroll', () => {
    if (AppState.currentView === 'reader') {
      const pct = calculateScrollPercent();
      document.getElementById('reader-progress-line').style.width = `${pct}%`;
    }
  });

  // Mark as Completed button
  document.getElementById('btn-mark-complete').addEventListener('click', async () => {
    const btn = document.getElementById('btn-mark-complete');
    const isNowCompleted = !btn.classList.contains('is-completed');

    if (isNowCompleted) {
      btn.classList.add('is-completed');
      btn.innerHTML = '✓ Unit Completed';
      showCelebrationToast('🎉 Unit Completed! Great progress!');
      await syncReadingProgress(true);
    } else {
      btn.classList.remove('is-completed');
      btn.innerHTML = 'Mark Unit as Completed ★';
      await syncReadingProgress(false);
    }
  });

  // Notes drawer autosave
  document.getElementById('unit-notes-input').addEventListener('input', (e) => {
    clearTimeout(AppState.noteDebounceTimer);
    AppState.noteDebounceTimer = setTimeout(async () => {
      if (!AppState.activeCourse || !AppState.activeUnit) return;
      const noteContent = e.target.value;
      await fetch(`/api/notes/${AppState.activeCourse}/${AppState.activeUnit}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ note_content: noteContent })
      });
    }, 700);
  });

  // Live Search Input
  let searchTimer;
  document.getElementById('search-input').addEventListener('input', (e) => {
    clearTimeout(searchTimer);
    const q = e.target.value.trim();
    if (q.length < 2) {
      document.getElementById('search-results-list').innerHTML = '';
      return;
    }
    searchTimer = setTimeout(async () => {
      const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
      const results = await res.json();
      renderSearchResults(results);
    }, 300);
  });
}

function switchView(viewName) {
  AppState.currentView = viewName;

  // Toggle main sections
  document.getElementById('view-home').style.display = viewName === 'home' ? 'block' : 'none';
  document.getElementById('view-courses').style.display = viewName === 'courses' ? 'block' : 'none';
  document.getElementById('view-roadmap').style.display = viewName === 'roadmap' ? 'block' : 'none';
  document.getElementById('view-reader').classList.toggle('active', viewName === 'reader');
  document.getElementById('view-solutions').style.display = viewName === 'solutions' ? 'block' : 'none';
  document.getElementById('view-pdf').style.display = viewName === 'pdf' ? 'block' : 'none';

  // Toggle bottom nav bar (hidden during reading for immersion)
  document.querySelector('.bottom-nav').style.display = viewName === 'reader' ? 'none' : 'flex';
  document.querySelector('.app-header').style.display = viewName === 'reader' ? 'none' : 'flex';

  // Update nav item active states
  document.querySelectorAll('.bottom-nav .nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === viewName);
  });

  window.scrollTo(0, 0);
}

function calculateScrollPercent() {
  const h = document.documentElement.scrollHeight - window.innerHeight;
  if (h <= 0) return 0;
  return Math.min(100, Math.round((window.scrollY / h) * 100));
}

function togglePdfView(pdfPath) {
  const pdfFrame = document.getElementById('pdf-viewer-frame');
  pdfFrame.src = `/pdf/${pdfPath}`;
  switchView('pdf');
}

// --- Drawers & Settings ---

function openDrawer(drawerId) {
  document.getElementById('drawer-backdrop').classList.add('active');
  document.getElementById(drawerId).classList.add('active');
}

function closeAllDrawers() {
  document.getElementById('drawer-backdrop').classList.remove('active');
  document.querySelectorAll('.drawer').forEach(d => d.classList.remove('active'));
}

function applyTheme(themeName) {
  document.documentElement.setAttribute('data-theme', themeName);
  AppState.theme = themeName;
  localStorage.setItem('lumina_theme', themeName);
  document.querySelectorAll('.theme-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.theme === themeName);
  });
}

function applyTypography(size, family) {
  AppState.fontSize = size;
  AppState.fontFamily = family;
  localStorage.setItem('lumina_font_size', size);
  localStorage.setItem('lumina_font_family', family);

  document.documentElement.style.setProperty('--reader-font-size', `${size}px`);
  const fontMap = {
    'sans': 'var(--font-sans)',
    'serif': 'var(--font-serif)',
    'mono': 'var(--font-mono)'
  };
  document.documentElement.style.setProperty('--reader-font-family', fontMap[family] || 'var(--font-sans)');
}

function showCelebrationToast(msg) {
  const toast = document.createElement('div');
  toast.className = 'celebration-toast';
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2500);
}

function renderSearchResults(results) {
  const container = document.getElementById('search-results-list');
  if (!results.length) {
    container.innerHTML = '<p class="reader-p" style="color:var(--text-muted);">No matching modules found.</p>';
    return;
  }

  let html = '';
  results.forEach(r => {
    html += `
      <div class="search-result-item" onclick="closeAllDrawers(); loadUnit('${r.course_code}', '${r.unit_id}')">
        <div style="font-size:11px; font-weight:700; color:var(--primary);">${r.course_code}: ${r.unit_num}</div>
        <div style="font-size:14px; font-weight:700;">${r.title}</div>
        <div style="font-size:12px; color:var(--text-muted);">${r.course_title} • ~${r.est_read_time}m read</div>
      </div>
    `;
  });
  container.innerHTML = html;
}

function showLoading() {
  // Optional lightweight loading spinner indicator
}

function hideLoading() {
  // Optional hide loading
}

function escapeHtml(text) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return text.replace(/[&<>"']/g, m => map[m]);
}
