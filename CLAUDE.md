# CLAUDE.md - AI Assistant Development Guide

> **Last Updated:** 2026-01-22
> **Project:** Pronostici Calcio - Football Matches Dashboard
> **Tech Stack:** HTML5, CSS3, Vanilla JavaScript (ES6+)
> **Architecture:** Single-file application (no build tools)

---

## 1. Project Overview

### Purpose
**Pronostici Calcio** is a modern, beautiful football matches dashboard that displays today's matches from major European leagues. It serves as both a functional web application and an educational reference for web development fundamentals.

### Key Characteristics
- **Single-file architecture**: Everything in `index.html` (HTML + CSS + JS)
- **No dependencies**: Zero external libraries or frameworks
- **No build process**: Direct browser execution
- **Fake data**: 12 hardcoded matches for demonstration
- **Modern design**: Gradient backgrounds, card layouts, hover effects
- **Responsive**: Works on all screen sizes (mobile, tablet, desktop)

### Target Audience
- Web developers building portfolio projects
- Learners studying HTML/CSS/JavaScript
- Anyone needing a quick football matches display

---

## 2. Repository Structure

```
pronostici-calcio/
├── index.html          # Main application (440+ lines)
├── README.md          # User-facing documentation
└── CLAUDE.md          # This file - AI assistant guide
```

### File Breakdown

**`index.html`** (~440 lines total)
- **Lines 1-10**: HTML document setup and meta tags
- **Lines 11-193**: Embedded CSS styling
- **Lines 194-223**: HTML structure (header, containers, stats section)
- **Lines 224-440**: JavaScript logic (data, rendering, statistics)

---

## 3. Code Architecture

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pronostici Calcio - Today's Football Matches</title>
    <style>
        /* All CSS here (~180 lines) */
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>⚽ Pronostici Calcio</h1>
            <p>Today's Top Football Matches</p>
        </header>

        <div id="matches-container" class="matches-grid">
            <!-- JavaScript renders match cards here -->
        </div>

        <div class="stats-section">
            <!-- Statistics dashboard -->
        </div>
    </div>

    <script>
        /* All JavaScript here (~200 lines) */
    </script>
</body>
</html>
```

### CSS Architecture

**Design System:**
- **Colors:**
  - Primary gradient: `#667eea` → `#764ba2` (purple-blue)
  - Accent red: `#e74c3c` (time highlights)
  - Text dark: `#2c3e50`
  - Text light: `#7f8c8d`
  - Background white: `#ffffff`

- **Typography:**
  - Font family: `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`
  - Header: `2.5em`
  - Team names: `1.1em`, bold
  - Details: `0.9em`

- **Spacing:**
  - Container max-width: `1200px`
  - Card padding: `25px`
  - Grid gap: `25px`
  - Border radius: `15px` (cards), `10px` (smaller elements)

- **Layout:**
  - CSS Grid for matches: `repeat(auto-fill, minmax(350px, 1fr))`
  - Flexbox for team alignment
  - Responsive breakpoint: `768px`

**Key CSS Classes:**
```css
.container          → Main wrapper, centered with max-width
.matches-grid       → CSS Grid container for match cards
.match-card         → Individual match card with hover effects
.league-badge       → Small gradient pill for league name
.match-time         → Red highlighted match time
.teams              → Flexbox container for home vs away
.team               → Individual team (name + emoji)
.vs                 → "VS" separator
.match-details      → Stadium and referee info
.stats-section      → Statistics dashboard at bottom
.stat-card          → Individual statistic with number + label
```

### JavaScript Data Model

**Match Object Structure:**
```javascript
{
    homeTeam: string,      // Required: Home team name
    awayTeam: string,      // Required: Away team name
    homeEmoji: string,     // Required: Emoji representing home team
    awayEmoji: string,     // Required: Emoji representing away team
    time: string,          // Required: Match time in "HH:MM" format
    league: string,        // Required: League name
    stadium: string,       // Required: Stadium name
    referee: string        // Required: Referee name
}
```

**Sample Data:**
```javascript
const matches = [
    {
        homeTeam: "Manchester United",
        awayTeam: "Liverpool",
        homeEmoji: "🔴",
        awayEmoji: "🔴",
        time: "15:00",
        league: "Premier League",
        stadium: "Old Trafford",
        referee: "Michael Oliver"
    },
    // ... 11 more matches
];
```

**Current Dataset:**
- 12 total matches
- 5 leagues (Premier League, La Liga, Bundesliga, Serie A, Ligue 1)
- 24 unique teams
- Times range from 15:00 to 21:00

### JavaScript Functions

**`renderMatches()` (Lines ~351-381)**
- Loops through `matches` array using `forEach`
- Generates HTML string for each match using template literals
- Appends to `#matches-container` using `innerHTML +=`
- Creates match cards with all details

**`calculateStats()` (Lines ~383-401)**
- Counts total matches: `matches.length`
- Calculates unique leagues: `new Set(matches.map(...))`
- Counts unique teams: Extracts all teams, creates Set
- Updates DOM elements: `#total-matches`, `#total-leagues`, `#total-teams`

**Initialization (Lines ~403-405)**
```javascript
renderMatches();
calculateStats();
```

---

## 4. Development Workflows

### Making Changes

#### 1. Adding New Matches
**Location:** `index.html` (lines ~237-338)

Add to the `matches` array:
```javascript
{
    homeTeam: "New Team",
    awayTeam: "Opponent",
    homeEmoji: "🔵",
    awayEmoji: "🟡",
    time: "16:00",
    league: "League Name",
    stadium: "Stadium Name",
    referee: "Referee Name"
}
```

**Effects:**
- New card appears in grid automatically
- Statistics update automatically
- No other changes needed

#### 2. Modifying Styling

**Colors:** Lines 11-193
```css
/* Change main gradient */
background: linear-gradient(135deg, #newcolor1 0%, #newcolor2 100%);

/* Change time color */
.match-time { color: #newcolor; }
```

**Layout:**
```css
/* Change card minimum width */
.matches-grid {
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
}

/* Change container width */
.container { max-width: 1400px; }
```

**Spacing:**
```css
/* Adjust card padding */
.match-card { padding: 30px; }

/* Adjust grid gaps */
.matches-grid { gap: 30px; }
```

#### 3. Changing HTML Structure
**Location:** Lines 194-223

Current structure is minimal by design:
- Header with title
- Empty matches container (filled by JS)
- Stats section with placeholders

**To add new sections:**
```html
<div class="new-section">
    <!-- Your content here -->
</div>
```

Add corresponding CSS and update JavaScript if needed.

#### 4. Modifying JavaScript Logic

**Rendering changes:** Lines ~351-381
- Modify template literal to change card structure
- Add/remove fields from display
- Change emoji sizes or positions

**Statistics changes:** Lines ~383-401
- Add new stat calculations
- Create new stat cards in HTML
- Update calculation logic

### Testing Workflow

1. **Save** `index.html`
2. **Open/Refresh** in browser
3. **Check console** (F12 → Console) for errors
4. **Test responsive** (F12 → Device Toolbar)
5. **Verify calculations** (count matches, leagues, teams manually)

**No build step required!**

---

## 5. Code Conventions

### Naming Conventions

**CSS:**
- Classes: `kebab-case` (`.match-card`, `.league-badge`, `.team-name`)
- IDs: `kebab-case` (`#matches-container`, `#total-matches`)

**JavaScript:**
- Variables: `camelCase` (`matchesContainer`, `homeTeam`, `awayTeam`)
- Functions: `camelCase` (`renderMatches()`, `calculateStats()`)
- Constants: `camelCase` (`matches`)

**HTML:**
- IDs: `kebab-case`
- Classes: `kebab-case`

### Code Style

**Indentation:** 4 spaces

**Quotes:**
- HTML attributes: Double quotes `class="example"`
- CSS properties: No quotes (except in `content` or URLs)
- JavaScript strings: Double quotes `"string"` or template literals `` `${var}` ``

**Semicolons:** Always used in JavaScript

**Spacing:**
- Space after `:` in CSS: `color: red;`
- Space around operators: `a = b + c`
- No space before function parentheses: `function name()`

### Comments

**CSS:**
```css
/* Section header comment */
.class-name {
    /* Inline explanation if needed */
}
```

**JavaScript:**
```javascript
// Single line comment for brief explanations

// Function description
function renderMatches() {
    // Implementation details
}
```

**Minimal comments** - Code should be self-documenting when possible.

---

## 6. AI Assistant Guidelines

### DO:

✅ **Maintain single-file architecture**
- Keep everything in `index.html`
- Don't suggest splitting into separate files unless explicitly requested

✅ **Preserve the modern design aesthetic**
- Keep gradient backgrounds
- Maintain card-based layout
- Preserve hover effects and transitions

✅ **Keep data structure consistent**
- All matches should have the same 8 properties
- Use proper emoji format for team colors

✅ **Update both rendering AND statistics**
- If adding/removing matches, verify stats still calculate correctly
- Test that unique counts work properly

✅ **Test responsive design**
- Verify changes work on mobile (768px and below)
- Ensure grid layout adapts properly

✅ **Use modern CSS/JS features**
- CSS Grid, Flexbox
- Template literals
- Arrow functions
- Set data structure

✅ **Provide code locations**
- Reference specific line numbers or ranges
- Use format: `index.html:237-338`

### DON'T:

❌ **Add build tools or dependencies**
- No npm, webpack, babel, etc.
- No external CSS frameworks (Bootstrap, Tailwind)
- No JavaScript libraries (jQuery, React, Vue)

❌ **Create separate files**
- Don't split CSS into external stylesheet
- Don't create separate JS files
- Keep single-file architecture

❌ **Add real API calls** (unless explicitly requested)
- Project uses fake data intentionally
- Adding APIs adds complexity and dependencies

❌ **Over-engineer solutions**
- Keep it simple and maintainable
- Don't add state management, routers, etc.
- Solution should fit in one file

❌ **Break responsive design**
- Don't use fixed widths that break mobile
- Test changes at multiple screen sizes

❌ **Remove visual polish**
- Keep gradients, shadows, hover effects
- Maintain modern aesthetic

❌ **Add backend functionality**
- No databases, servers, authentication (unless requested)
- This is a frontend-only project

### When Suggesting Changes:

1. **Explain the impact**: What will change and why
2. **Show code location**: Specific line numbers
3. **Provide complete code**: Don't use `...` or omit parts
4. **Consider side effects**: Stats, layout, responsiveness
5. **Test mentally**: Will this work in the browser?

---

## 7. Common Modification Patterns

### Pattern 1: Adding a Match

**Location:** `index.html:237-338` (matches array)

```javascript
// Add after the last match
{
    homeTeam: "Newcastle United",
    awayTeam: "Aston Villa",
    homeEmoji: "⚫",
    awayEmoji: "🔵",
    time: "14:00",
    league: "Premier League",
    stadium: "St James' Park",
    referee: "Simon Hooper"
}
```

**Effect:**
- Automatically renders in grid
- Statistics update (total matches, possibly teams)

### Pattern 2: Changing Color Scheme

**Location:** `index.html:11-193` (CSS section)

**Example: Green theme**
```css
body {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}

.league-badge {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}

.stat-card {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}
```

### Pattern 3: Adding a New Statistic

**Step 1:** Add HTML element (lines ~212-220)
```html
<div class="stat-card">
    <div class="stat-number" id="avg-time">0</div>
    <div class="stat-label">Average Match Time</div>
</div>
```

**Step 2:** Add calculation logic (lines ~383-401)
```javascript
function calculateStats() {
    // ... existing code ...

    // Calculate average time
    const times = matches.map(m => {
        const [hours, minutes] = m.time.split(':').map(Number);
        return hours * 60 + minutes;
    });
    const avgMinutes = times.reduce((a, b) => a + b) / times.length;
    const avgHours = Math.floor(avgMinutes / 60);
    const avgMins = Math.round(avgMinutes % 60);
    document.getElementById('avg-time').textContent =
        `${avgHours}:${avgMins.toString().padStart(2, '0')}`;
}
```

### Pattern 4: Filtering by League

**Add filter buttons in HTML:** (after header, line ~201)
```html
<div class="filters">
    <button class="filter-btn" onclick="filterLeague('all')">All</button>
    <button class="filter-btn" onclick="filterLeague('Premier League')">Premier League</button>
    <button class="filter-btn" onclick="filterLeague('La Liga')">La Liga</button>
    <!-- ... more buttons ... -->
</div>
```

**Add CSS for buttons:** (in style section)
```css
.filters {
    text-align: center;
    margin-bottom: 30px;
}

.filter-btn {
    background: white;
    border: 2px solid #667eea;
    color: #667eea;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
}

.filter-btn:hover,
.filter-btn.active {
    background: #667eea;
    color: white;
}
```

**Add filter function in JavaScript:**
```javascript
function filterLeague(league) {
    const filtered = league === 'all'
        ? matches
        : matches.filter(m => m.league === league);

    matchesContainer.innerHTML = '';
    filtered.forEach(match => {
        // ... same rendering code ...
    });
}
```

### Pattern 5: Adding Team Logos

**Step 1:** Add logo URLs to match objects
```javascript
{
    homeTeam: "Manchester United",
    awayTeam: "Liverpool",
    homeLogo: "https://example.com/mu-logo.png",
    awayLogo: "https://example.com/lfc-logo.png",
    // ... rest of properties
}
```

**Step 2:** Update rendering template (line ~354+)
```javascript
const matchCard = `
    <div class="match-card">
        <!-- ... -->
        <div class="team">
            <img src="${match.homeLogo}" alt="${match.homeTeam}" class="team-logo-img">
            <div class="team-name">${match.homeTeam}</div>
        </div>
        <!-- ... -->
    </div>
`;
```

**Step 3:** Add CSS for images
```css
.team-logo-img {
    width: 60px;
    height: 60px;
    object-fit: contain;
    margin-bottom: 10px;
}
```

---

## 8. Technical Details

### Browser Compatibility

**Fully Supported:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Not Supported:**
- Internet Explorer (any version)

**Reason:** Uses ES6+ features (template literals, arrow functions, Set, const/let)

### Performance Characteristics

**Load Performance:**
- Single HTTP request
- File size: ~8-10KB
- Zero external dependencies
- Instant rendering (synchronous)

**Runtime Performance:**
- O(n) rendering: Linear with number of matches
- O(n) statistics: Single pass through data
- No memory leaks: No event listeners to clean up
- No API calls: Zero network overhead

**Scalability:**
- Suitable for: 1-100 matches
- Beyond 100: Consider pagination or virtualization
- Current: 12 matches (optimal)

### Accessibility Status

**Current Implementation:**
- ✅ Semantic HTML
- ✅ Responsive viewport
- ✅ Color contrast (meets WCAG AA)
- ✅ Readable fonts

**Missing (Potential Improvements):**
- ❌ ARIA labels for dynamic content
- ❌ Keyboard navigation focus styles
- ❌ Screen reader announcements
- ❌ Focus management
- ❌ Skip navigation links
- ❌ Reduced motion support

**To Add Basic Accessibility:**
```html
<div class="match-card" role="article" aria-label="Match: ${homeTeam} vs ${awayTeam}">
```

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## 9. Data Reference

### Current Matches Dataset

**Leagues Distribution:**
- Premier League: 3 matches
- La Liga: 3 matches
- Bundesliga: 2 matches
- Serie A: 2 matches
- Ligue 1: 2 matches

**Teams Included:**
Premier League: Manchester United, Liverpool, Chelsea, Arsenal, Tottenham, Manchester City
La Liga: Real Madrid, Barcelona, Atletico Madrid, Sevilla, Valencia, Real Betis
Bundesliga: Bayern Munich, Borussia Dortmund, RB Leipzig, Bayer Leverkusen
Serie A: Juventus, AC Milan, Inter Milan, Napoli
Ligue 1: Paris Saint-Germain, Marseille, Lyon, Monaco

**Time Range:** 15:00 - 21:00

**Emoji Legend:**
- 🔴 = Red/Red teams
- 🔵 = Blue teams
- ⚪ = White teams
- ⚫ = Black teams
- 🟡 = Yellow teams
- 🟢 = Green teams

---

## 10. Debugging Guide

### Common Issues

**Issue: Matches don't appear**
- **Check:** Browser console (F12)
- **Likely cause:** JavaScript syntax error in matches array
- **Fix:** Look for missing commas, quotes, or braces

**Issue: Layout breaks on mobile**
- **Check:** Responsive design mode (F12 → Toggle device toolbar)
- **Likely cause:** Fixed widths or min-width too large
- **Fix:** Verify `minmax(350px, 1fr)` in grid definition

**Issue: Stats show wrong numbers**
- **Check:** Console log the calculations
- **Likely cause:** Duplicate teams or incorrect Set usage
- **Fix:** Verify unique team extraction logic

**Issue: Hover effects don't work**
- **Check:** CSS transitions and transforms
- **Likely cause:** Browser doesn't support CSS transforms
- **Fix:** Test in modern browser (Chrome, Firefox, Safari)

**Issue: Colors look wrong**
- **Check:** CSS gradient syntax
- **Likely cause:** Invalid hex colors or gradient syntax
- **Fix:** Verify hex codes start with `#` and have 6 digits

### Debugging Tools

**Browser DevTools (F12):**
- **Console:** JavaScript errors and logs
- **Elements:** Inspect HTML/CSS, live edit
- **Network:** Verify file loaded (should be one request)
- **Device Toolbar:** Test responsive design

**Validation:**
- HTML: https://validator.w3.org/
- CSS: https://jigsaw.w3.org/css-validator/

**Testing Checklist:**
- [ ] Opens in browser without errors
- [ ] All 12 matches display
- [ ] Statistics show correct numbers (12 matches, 5 leagues, 24 teams)
- [ ] Hover effects work on cards
- [ ] Responsive on mobile (test at 375px width)
- [ ] No console errors or warnings

---

## 11. Extension Ideas

### Beginner Extensions (No new concepts)

**Easy:**
- Add more matches to the array
- Change team emojis
- Modify color scheme
- Change stadium names

**Medium:**
- Add a "Featured Match" section
- Sort matches by time
- Add match day/date display
- Create league filter buttons

### Intermediate Extensions (New CSS/JS)

**Moderate:**
- Add dark mode toggle
- Implement search functionality
- Add sorting controls
- Create printable stylesheet
- Add team logos (images)
- Implement local storage for favorites

**Advanced:**
- Add animations on page load
- Create a countdown timer to next match
- Build a predictions form
- Add match result display
- Implement progressive web app (PWA)

### Advanced Extensions (APIs/Backend)

**Complex:**
- Connect to real football API
- Add live score updates (WebSocket)
- Implement user authentication
- Create betting odds integration
- Build admin dashboard
- Add database persistence
- Create REST API backend

**Note:** Only suggest advanced extensions if user explicitly requests them. Default to keeping it simple.

---

## 12. Quick Reference Tables

### File Structure
| File | Purpose | Lines | Size |
|------|---------|-------|------|
| `index.html` | Complete application | ~440 | ~8KB |
| `README.md` | User documentation | ~200 | ~6KB |
| `CLAUDE.md` | AI assistant guide | ~900 | ~15KB |

### Code Sections in index.html
| Section | Line Range | Description |
|---------|------------|-------------|
| HTML Setup | 1-10 | DOCTYPE, meta tags, title |
| CSS Styles | 11-193 | All styling rules |
| HTML Body | 194-223 | Structure and containers |
| JavaScript | 224-440 | Data, logic, rendering |
| Match Data | 237-338 | `matches` array |
| Render Function | 351-381 | `renderMatches()` |
| Stats Function | 383-401 | `calculateStats()` |
| Initialization | 403-405 | Function calls |

### Color Palette
| Element | Color Code | Usage |
|---------|------------|-------|
| Gradient Start | `#667eea` | Purple (backgrounds) |
| Gradient End | `#764ba2` | Darker purple |
| Time Highlight | `#e74c3c` | Red (match times) |
| Primary Text | `#2c3e50` | Dark gray (main text) |
| Secondary Text | `#7f8c8d` | Light gray (details) |
| Card Background | `#ffffff` | White |
| Light Gray | `#ecf0f1` | Borders |
| Muted Gray | `#95a5a6` | VS text |

### CSS Classes Reference
| Class | Purpose | Key Properties |
|-------|---------|----------------|
| `.container` | Main wrapper | `max-width: 1200px` |
| `.matches-grid` | Grid container | `display: grid` |
| `.match-card` | Individual match | Padding, shadow, hover |
| `.league-badge` | League pill | Gradient background |
| `.match-time` | Time display | Red color, bold |
| `.teams` | Flexbox container | `justify-content: space-between` |
| `.team` | Team info | Centered text |
| `.team-name` | Team name | Bold, 1.1em |
| `.team-logo` | Emoji | 2.5em size |
| `.vs` | Separator | Gray, 1.5em |
| `.match-details` | Stadium/referee | Border top, flex |
| `.stats-section` | Stats container | White background |
| `.stat-card` | Individual stat | Gradient, centered |
| `.stat-number` | Stat value | 2.5em, bold |
| `.stat-label` | Stat description | 1em, white |

### JavaScript Data Schema
```typescript
// TypeScript-style definition (for reference only)
interface Match {
    homeTeam: string;      // "Manchester United"
    awayTeam: string;      // "Liverpool"
    homeEmoji: string;     // "🔴"
    awayEmoji: string;     // "🔴"
    time: string;          // "15:00" (HH:MM format)
    league: string;        // "Premier League"
    stadium: string;       // "Old Trafford"
    referee: string;       // "Michael Oliver"
}

const matches: Match[] = [...];
```

### Key Functions API
```javascript
// Renders all matches to the DOM
function renderMatches(): void

// Calculates and displays statistics
function calculateStats(): void

// Global data
const matches: Match[]
const matchesContainer: HTMLElement
```

---

## 13. AI Assistant Best Practices

### When User Asks to "Add Feature X"

1. **Assess complexity**
   - Can it be done in single-file?
   - Does it need external dependencies?
   - Is it within scope?

2. **Explain before implementing**
   - What will change?
   - Which sections of code?
   - Any side effects?

3. **Provide complete code**
   - Don't use `...` or omit code
   - Show exact line numbers
   - Include all necessary changes

4. **Test mentally**
   - Will this work in browser?
   - Any syntax errors?
   - Responsive design maintained?

5. **Update documentation**
   - Should README.md be updated?
   - Any new conventions?

### When User Reports a Bug

1. **Reproduce the issue**
   - What should happen?
   - What actually happens?
   - Which browser/device?

2. **Identify root cause**
   - Read the relevant code
   - Check console errors
   - Verify data structure

3. **Propose fix**
   - Show exact code change
   - Explain why it fixes the issue
   - Mention alternative approaches

4. **Prevent recurrence**
   - Suggest validation
   - Add error handling if needed
   - Recommend testing approach

### When User Wants to Learn

1. **Start with concepts**
   - Explain HTML/CSS/JS roles
   - Use analogies and examples
   - Link to MDN documentation

2. **Point to specific code**
   - Use `index.html:line` format
   - Show relevant sections
   - Explain how it works

3. **Encourage experimentation**
   - "Try changing X to Y"
   - "What happens if you remove this?"
   - Safe areas to modify

4. **Progressive complexity**
   - Start simple (change colors)
   - Build up (add matches)
   - Advanced (new features)

### Communication Style

- **Be direct**: Clear, concise answers
- **Be specific**: Line numbers, exact code
- **Be complete**: Full code blocks, not snippets
- **Be accurate**: Test suggestions mentally
- **Be helpful**: Offer next steps

---

## 14. Project Metadata

**Project Name:** Pronostici Calcio
**Version:** 1.0.0 (informal)
**Created:** 2026-01-22
**Last Updated:** 2026-01-22
**Author:** Claude (AI Assistant)
**License:** MIT (implied open source)
**Language:** HTML, CSS, JavaScript
**Browser Target:** Modern browsers (ES6+ support)
**File Size:** ~8KB (single file)
**Dependencies:** None
**Build Tool:** None required

---

## 15. Additional Resources

### For Users
- **README.md**: User-facing documentation
- **index.html**: View source to learn implementation
- **Browser DevTools**: F12 to inspect and experiment

### For Learning
- **MDN Web Docs**: https://developer.mozilla.org/
- **CSS Tricks**: https://css-tricks.com/
- **JavaScript.info**: https://javascript.info/

### For APIs (Future)
- **API-Football**: https://www.api-football.com/
- **Football-Data.org**: https://www.football-data.org/
- **SportRadar**: https://developer.sportradar.com/

---

**End of CLAUDE.md**

---

> **For AI Assistants**: This guide is your complete reference for working with this project. Always prioritize:
> 1. **Single-file architecture** - No separate files
> 2. **No dependencies** - Keep it vanilla
> 3. **Modern design** - Maintain visual quality
> 4. **Code clarity** - Easy to understand
> 5. **User intent** - Ask if unsure
>
> When in doubt, keep it simple and ask the user for clarification.
