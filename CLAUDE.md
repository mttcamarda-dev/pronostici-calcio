# CLAUDE.md - AI Assistant Guide for Pronostici-Calcio

## Project Overview

**Pronostici-Calcio** (Italian for "Football Predictions") is an educational static website project designed for complete beginners learning web development. The project displays football match information in a clean, simple interface.

**Key Characteristics:**
- **Type**: Static single-page application (SPA)
- **Complexity**: Beginner-level educational project
- **Architecture**: Single-file HTML with embedded CSS and JavaScript
- **Dependencies**: Zero - pure vanilla HTML/CSS/JavaScript
- **Build Process**: None - runs directly in browser
- **Target Audience**: Complete beginners to web development

## Repository Structure

```
pronostici-calcio/
├── .git/              # Git version control
├── index.html         # Main application file (134 lines)
├── README.md          # Beginner-focused documentation (56 lines)
└── CLAUDE.md          # This file - AI assistant guide
```

**Total Lines of Code**: ~134 lines in a single file

## Technology Stack

### Core Technologies (No Frameworks)
- **HTML5**: Semantic markup, viewport meta tag for mobile responsiveness
- **CSS3**: Embedded styling with modern features (box-shadow, border-radius)
- **JavaScript (ES6)**: Client-side rendering with arrow functions, template literals

### Notable Absences
- No package.json or Node.js dependencies
- No build tools (webpack, vite, rollup)
- No CSS preprocessors (SASS, Less)
- No JavaScript frameworks (React, Vue, Angular)
- No testing framework
- No linting/formatting tools
- No .gitignore file

## Code Architecture

### Single-File Structure (index.html)

The file is organized in three clear sections:

1. **HTML Structure** (lines 1-73)
   - DOCTYPE and semantic HTML5 markup
   - Minimal DOM elements: container → match cards → content
   - Empty `<div id="matches-container">` populated by JavaScript

2. **CSS Styling** (lines 9-63, in `<style>` tag)
   - Embedded in `<head>` section
   - BEM-like class naming: `.container`, `.match`, `.teams`, `.details`, `.time`
   - Card-based UI pattern with visual depth

3. **JavaScript Logic** (lines 76-132, in `<script>` tag at bottom)
   - Data array with 5 sample matches
   - DOM manipulation to render matches dynamically
   - Imperative programming style (beginner-friendly)

## Coding Conventions

### CSS Patterns
- **Class Naming**: kebab-case (`.match`, `.teams`, `.details`)
- **Color Palette**: Consistent theme
  - Primary dark: `#2c3e50`
  - Accent blue: `#3498db`
  - Accent red: `#e74c3c`
  - Backgrounds: `#ecf0f1`, `#f8f9fa`
- **Layout**: Centered container with `max-width: 800px`
- **Typography**: System fonts, responsive sizing
- **Components**: Card-based design with shadows and rounded corners

### JavaScript Patterns
- **Naming**: camelCase for variables (`homeTeam`, `awayTeam`, `matchHTML`)
- **Data Structure**: Array of objects with consistent schema
  ```javascript
  {
    homeTeam: String,
    awayTeam: String,
    time: String,
    league: String
  }
  ```
- **String Building**: Template literals with embedded expressions
- **DOM Updates**: `.innerHTML +=` (note: inefficient but beginner-friendly)
- **Comments**: Verbose, beginner-oriented explanations

### HTML Patterns
- **Semantic Tags**: Proper use of `<h1>`, `<div>`, structural elements
- **Emojis**: Visual feedback (⚽, ⏰, 🏆) for beginner appeal
- **Accessibility**: Basic viewport meta tag, semantic structure

## Current Features

The application currently displays 5 hardcoded football matches:
1. Manchester United vs Liverpool (Premier League)
2. Real Madrid vs Barcelona (La Liga)
3. Bayern Munich vs Borussia Dortmund (Bundesliga)
4. Juventus vs AC Milan (Serie A)
5. PSG vs Marseille (Ligue 1)

## Development Workflows

### Making Changes

**Since this is a zero-build project:**
1. Edit `index.html` directly
2. Refresh browser to see changes
3. No compilation or build step needed

**Testing Changes:**
1. Open `index.html` in a web browser (double-click or `open index.html`)
2. Use browser DevTools for debugging
3. Check responsive design with device emulation

### Git Workflow

**Branch Strategy:**
- Develop on feature branches with pattern: `claude/claude-md-*`
- Current branch: `claude/claude-md-mkq4vxh62jver15l-kilz8`
- Main branch: Not explicitly set in current configuration

**Commit Guidelines:**
- Use clear, descriptive commit messages
- Current style: "Create simple football matches website for beginners"
- Focus on what and why, keep messages concise

**Push Protocol:**
- Always use: `git push -u origin <branch-name>`
- Branch names must start with `claude/` and match session ID
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) on network errors

## AI Assistant Guidelines

### Core Principles

1. **Preserve Simplicity**: This is a beginner project - avoid adding complexity
2. **No Dependencies**: Do NOT introduce npm, frameworks, or libraries unless explicitly requested
3. **Educational Focus**: Maintain verbose comments and beginner-friendly code style
4. **Single-File Architecture**: Keep everything in `index.html` unless there's a compelling reason to split

### When Adding Features

**DO:**
- Use vanilla JavaScript - no jQuery, React, or frameworks
- Add extensive comments explaining new code
- Keep data structures simple and readable
- Maintain the existing visual style and color scheme
- Test in browser before committing
- Update README.md if adding significant features

**DON'T:**
- Add build tools or compilation steps
- Introduce external dependencies
- Use advanced ES6+ features that require transpilation
- Over-engineer solutions
- Add complex state management
- Create separate CSS/JS files without discussion
- Sacrifice code clarity for performance

### Common Modification Scenarios

#### Adding New Matches
```javascript
// Add to the matches array in index.html
matches.push({
  homeTeam: "Team A",
  awayTeam: "Team B",
  time: "HH:MM",
  league: "League Name"
});
```

#### Adding New Fields
1. Update match object structure
2. Modify the template literal in `matchHTML`
3. Add corresponding CSS for new elements
4. Update comments to explain new fields

#### Styling Changes
1. Modify the `<style>` section in `<head>`
2. Maintain existing class naming conventions
3. Keep mobile responsiveness (max-width: 800px)
4. Test on multiple screen sizes

#### Adding Interactivity
1. Add event listeners in the `<script>` section
2. Use vanilla JavaScript only (no jQuery)
3. Comment extensively for beginners
4. Keep logic simple and readable

### Code Quality Considerations

**Current Known Issues** (acceptable for beginners, but note for improvements):

1. **Performance**: Using `.innerHTML +=` in a loop causes multiple DOM reflows
   - **Better approach**: Build complete HTML string, then set once
   - **When to fix**: If adding many more matches (>50)

2. **Security**: `.innerHTML` with untrusted data poses XSS risks
   - **Current state**: Safe (hardcoded data)
   - **When to fix**: If adding user input or external data

3. **Maintainability**: All code in one file
   - **Current state**: Appropriate for beginner project
   - **When to fix**: Only if project grows beyond ~300 lines

### Recommended Improvements (If Requested)

**Low-Hanging Fruit:**
1. Add `.gitignore` file for common development artifacts
2. Fetch match data from a JSON file or API
3. Add search/filter functionality
4. Implement match predictions (align with project name)
5. Add local storage for user preferences
6. Make matches sortable by league, time, or team

**Medium Complexity:**
1. Split into separate HTML/CSS/JS files
2. Add form to add custom matches
3. Implement responsive grid layout
4. Add match status (upcoming, live, finished)
5. Create print-friendly stylesheet

**Advanced (Requires Discussion):**
1. Add build process (Vite) for development experience
2. Introduce TypeScript for type safety
3. Add testing framework (Jest + Testing Library)
4. Connect to real football API (football-data.org)
5. Add PWA capabilities for offline use

### File Operations

**Reading Files:**
- Main file: `/home/user/pronostici-calcio/index.html`
- Documentation: `/home/user/pronostici-calcio/README.md`

**Creating New Files:**
- Avoid unless absolutely necessary
- If needed, update README.md with file inventory
- Consider impact on beginner-friendliness

**Editing index.html:**
- Always read the file first before suggesting changes
- Preserve the three-section structure (HTML/CSS/JS)
- Maintain indentation (2 spaces based on current code)
- Keep comments in beginner-friendly language

### Testing Protocol

**Manual Testing Checklist:**
1. Open `index.html` in browser
2. Verify all matches display correctly
3. Check responsive design (resize browser window)
4. Test in multiple browsers (Chrome, Firefox, Safari)
5. Verify console has no errors (F12 DevTools)

**No Automated Testing:**
- Project has no test framework
- Manual testing is appropriate for this scale
- Don't add testing infrastructure unless explicitly requested

### Deployment

**Current Deployment:**
- Simply open `index.html` in browser
- Can be uploaded to any static hosting

**Deployment Options:**
1. **GitHub Pages**: Enable in repo settings
2. **Netlify**: Drag and drop or Git integration
3. **Vercel**: Zero-config static deployment
4. **Cloudflare Pages**: Fast global CDN
5. **Local**: File system access via `file://`

**No Build Required:**
- All deployment platforms can serve `index.html` directly
- No build configuration needed

## Project Goals and Future Direction

**Based on Project Name** ("Pronostici" = Predictions):
- Likely intent to add match prediction features
- Could include score predictions, winner predictions
- Might add user voting or expert predictions
- Consider league tables, statistics

**Maintain Educational Value:**
- Any new features should remain beginner-accessible
- Add complexity gradually, with extensive documentation
- Keep README.md updated with learning resources

## Quick Reference Commands

```bash
# View the website
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows

# Check git status
git status

# Create and switch to new branch
git checkout -b claude/feature-name-sessionid

# Commit changes
git add index.html README.md
git commit -m "Descriptive commit message"

# Push changes
git push -u origin claude/branch-name

# View file structure
ls -la

# View file contents
cat index.html
```

## Troubleshooting

### Common Issues

**Issue**: Changes not appearing in browser
- **Solution**: Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

**Issue**: Emojis not displaying correctly
- **Solution**: Ensure file encoding is UTF-8

**Issue**: Push fails with 403
- **Solution**: Verify branch name starts with `claude/` and matches session ID

**Issue**: Layout broken on mobile
- **Solution**: Check viewport meta tag is present and CSS max-width is set

## Contact and Resources

**For Beginners:**
- MDN Web Docs: https://developer.mozilla.org
- JavaScript.info: https://javascript.info
- CSS-Tricks: https://css-tricks.com

**For AI Assistants:**
- Maintain beginner-friendly approach
- Explain technical decisions in simple terms
- Encourage learning and experimentation
- Avoid overwhelming with complexity

---

**Last Updated**: 2026-01-22
**Project Status**: Active development
**Beginner-Friendly**: Yes ✓
**Production-Ready**: Educational project, not intended for production
