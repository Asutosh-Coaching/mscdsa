# Lumina: MSCDSA Mobile Study & Reader System
### Mobile-First Learning, Reading, & Completion Platform for IGNOU M.Sc. Data Science and Analytics

Lumina transforms 6,000+ dense PDF pages across 12 IGNOU MSCDSA courses into a touch-optimized, distraction-free reading and study experience engineered specifically for mobile phones.

---

## 🌟 Why this solves reading books on Mobile

| Traditional PDF on Mobile | Lumina Mobile Reader System |
|:---|:---|
| ❌ Fixed A4/Letter size requires constant pinch-to-zoom and horizontal panning. | ✅ **Reflowable Responsive Typography**: Adapts dynamically to any phone screen size with custom font sizing (15px to 22px). |
| ❌ Dense black & white text causes severe eye strain after 15 minutes. | ✅ **Eye-Comfort Color Themes**: Sepia (Warm Paper), OLED Midnight (True Black for AMOLED battery saving), Clean Light, and Slate Dark. |
| ❌ Heavy reading fatigue; cannot study while walking, commuting, or resting. | ✅ **Audio Mode (Text-to-Speech)**: Integrated Web Speech engine reads lessons aloud at customizable speeds (1.0x, 1.25x, 1.5x, 2.0x). |
| ❌ Passive reading without retention verification. | ✅ **Interactive Self-Assessment Flashcards**: Flip cards extracted from IGNOU "Check Your Progress" checkpoints test comprehension before completion. |
| ❌ Lost reading position and no sense of curriculum progress. | ✅ **Smart Progress Tracking & Resume**: Remembers exact scroll position; tracks completed units, daily streaks, and study minutes in SQLite. |
| ❌ Separation of textbook theory and exam questions. | ✅ **Integrated Assignment Solutions**: Direct 1-tap cross-referencing to full solutions for all 12 courses. |
| ❌ Clunky app store downloads. | ✅ **Progressive Web App (PWA)**: Tap *"Add to Home Screen"* on iOS or Android for a full-screen, native-app feel. |

---

## 📱 How to Access on Your Mobile Phone

1. **Connect to the Same Wi-Fi Network:**
   Ensure your phone is connected to the same local Wi-Fi network as this computer.

2. **Open the Web Browser on your Phone:**
   Navigate to:
   ```
   http://192.168.1.104:8000
   ```
   *(Or on this desktop: `http://localhost:8000`)*

3. **Install as a Full-Screen App (PWA):**
   * **On iPhone (Safari):** Tap the **Share button** (square with upward arrow) $\to$ Select **"Add to Home Screen"** $\to$ Tap **"Add"**.
   * **On Android (Chrome):** Tap the **three-dots menu (⋮)** $\to$ Select **"Install app"** or **"Add to Home Screen"**.
   * *The Lumina app icon will now appear on your phone's home screen and launch full-screen without address bars!*

---

## 🛠️ Key System Features

### 1. Reflowable Reader with Quick Customization
- **Themes:** Sepia (Warm Paper), Light (Crisp White), Dark (Slate), Midnight OLED (True Black).
- **Font Sizing:** $A-$, $A$, $A+$ adjustments.
- **Font Families:** Modern Sans-Serif, Academic Serif (Merriweather), Monospace.
- **Visual Callouts:** Key definitions, theorems, formulas, and examples are automatically highlighted in visual badges.

### 2. Audio Mode (Hands-Free Listening)
- Tap the **🎧 Listen button** in the top bar of any unit.
- Reads through sections with natural voice synthesis.
- Adjust playback speed ($1.0\times$, $1.25\times$, $1.5\times$, $2.0\times$) or pause anytime.

### 3. Checkpoint Flashcards (Active Learning)
- At the end of every unit, interactive cards test key concepts from the syllabus.
- Tap any card to flip and reveal explanations and answers.

### 4. Personal Notes Drawer
- Tap the **📝 Note button** to slide out a personal notepad.
- Thoughts, summaries, and exam formulas autosave to the local database in real-time.

### 5. Original PDF Mode Toggle
- Need to verify a complex mathematical formula or original diagram? Tap the **📄 PDF icon** in the top bar to switch to the original IGNOU document view.

### 6. Course & Assignment Cross-Referencing
- Direct access to the complete assignment solution documents created in `assignment_solutions/` for every course.

---

## 🏗️ Architecture & File Structure

```
Resources/
├── mobile_reader_server.py      # FastAPI backend streaming APIs & PDF files
├── start_mobile_reader.bat      # Windows 1-click launcher
├── build_mobile_library.py      # Extraction script converting PDFs to structured units
├── mobile_reader/
│   ├── study_data.db            # SQLite database (progress, streaks, notes)
│   ├── curriculum.json          # Master curriculum manifest (12 courses, 112 units)
│   ├── db.py                    # Database connection and helper functions
│   ├── content/                 # Pre-extracted JSON units for instant sub-50ms loading
│   │   ├── MCS-061/ ...
│   │   └── MCS-224/ ...
│   └── static/
│       ├── index.html           # Single-Page Application shell
│       ├── styles.css           # Mobile-first CSS themes & animations
│       ├── app.js               # Client controller & Web Speech engine
│       ├── manifest.json        # PWA configuration
│       └── sw.js                # Service Worker for offline asset caching
```
