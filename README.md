# ⚽ Pronostici Calcio - Football Matches Dashboard

A beautiful, modern website displaying today's top football matches from major European leagues.

## 🌟 Features

- **Live Match Display**: Shows 12 exciting matches from top European leagues
- **Beautiful UI**: Modern gradient design with card-based layout
- **Match Details**: Includes team names, match times, stadiums, and referees
- **Statistics Dashboard**: Real-time stats showing total matches, leagues, and teams
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **No Dependencies**: Pure HTML, CSS, and JavaScript - no frameworks needed!

## 🎯 Leagues Covered

- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 **Premier League** (England)
- 🇪🇸 **La Liga** (Spain)
- 🇩🇪 **Bundesliga** (Germany)
- 🇮🇹 **Serie A** (Italy)
- 🇫🇷 **Ligue 1** (France)

## 🚀 Getting Started

### Option 1: View Locally

1. **Download the file**: Clone this repository or download `index.html`
2. **Open in browser**: Double-click `index.html` or drag it into your browser
3. **That's it!** The website will load instantly

### Option 2: Host Online

You can host this on any static hosting service:
- **GitHub Pages**: Free hosting for GitHub repositories
- **Netlify**: Drag and drop deployment
- **Vercel**: One-click deployment
- **AWS S3**: Static website hosting

Simply upload the `index.html` file and you're done!

## 📋 Sample Matches Included

The website currently displays fake data for demonstration purposes:

| Match | League | Time | Stadium |
|-------|--------|------|---------|
| Manchester United vs Liverpool | Premier League | 15:00 | Old Trafford |
| Real Madrid vs Barcelona | La Liga | 18:30 | Santiago Bernabéu |
| Bayern Munich vs Borussia Dortmund | Bundesliga | 20:00 | Allianz Arena |
| Juventus vs AC Milan | Serie A | 19:45 | Allianz Stadium |
| PSG vs Marseille | Ligue 1 | 21:00 | Parc des Princes |
| ...and 7 more exciting matches! | | | |

## 🛠️ Customization Guide

### Adding New Matches

Open `index.html` and locate the `matches` array (around line 237). Add a new match object:

```javascript
{
    homeTeam: "Team Name",
    awayTeam: "Opponent Name",
    homeEmoji: "🔴",
    awayEmoji: "🔵",
    time: "HH:MM",
    league: "League Name",
    stadium: "Stadium Name",
    referee: "Referee Name"
}
```

### Changing Colors

The color scheme is defined in the CSS section. Key colors:

```css
/* Main gradient background */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Time highlight */
color: #e74c3c;

/* Text colors */
color: #2c3e50;  /* Dark text */
color: #7f8c8d;  /* Light text */
```

### Modifying Layout

The layout uses CSS Grid for responsive design:

```css
.matches-grid {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 25px;
}
```

Adjust `minmax(350px, 1fr)` to change card width.

## 📱 Responsive Breakpoints

- **Desktop**: 3-4 columns (depending on screen width)
- **Tablet**: 2 columns
- **Mobile**: 1 column (below 768px)

The layout automatically adapts using CSS Grid's `auto-fill` feature.

## 🎨 Design Highlights

- **Modern Gradient**: Purple-blue gradient background
- **Card Hover Effects**: Cards lift up on hover with smooth transitions
- **Team Emojis**: Visual representation using colored circles
- **League Badges**: Stylish pills with gradient backgrounds
- **Shadow Depth**: Multiple layers of shadows for depth perception

## 🔧 Technical Details

### Technologies Used
- **HTML5**: Semantic markup
- **CSS3**: Modern features (Grid, Flexbox, Gradients, Transitions)
- **JavaScript ES6+**: Template literals, arrow functions, Set data structure

### Browser Support
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Internet Explorer: ❌ Not supported (uses modern ES6 features)

### Performance
- **Single HTTP request**: Everything in one file
- **File size**: ~8KB (tiny!)
- **Load time**: Instant on any connection
- **No external dependencies**: No CDN calls, no external libraries

## 📚 Code Structure

```
index.html
├── <head>
│   ├── Meta tags (charset, viewport)
│   └── <style> (CSS styling)
├── <body>
│   ├── Header (title and subtitle)
│   ├── Matches Grid (dynamically populated)
│   └── Statistics Section (calculated from data)
└── <script>
    ├── matches[] (data array)
    ├── renderMatches() (display function)
    └── calculateStats() (statistics function)
```

## 🎓 Learning Resources

This project is perfect for learning:

1. **HTML Structure**: Semantic elements and proper document structure
2. **CSS Grid & Flexbox**: Modern layout techniques
3. **CSS Gradients**: Beautiful visual effects
4. **JavaScript DOM Manipulation**: Dynamic content rendering
5. **Template Literals**: Modern string formatting
6. **Array Methods**: forEach, map, Set for data processing

## 🚀 Next Steps & Enhancement Ideas

### Beginner Level
- [ ] Add more matches to the array
- [ ] Change team colors and emojis
- [ ] Modify the color scheme
- [ ] Add your favorite teams

### Intermediate Level
- [ ] Add filter buttons by league
- [ ] Implement search functionality
- [ ] Sort matches by time
- [ ] Add team logos (image files)
- [ ] Create a dark mode toggle

### Advanced Level
- [ ] Connect to a real football API (e.g., API-Football)
- [ ] Add live score updates with WebSocket
- [ ] Implement betting odds display
- [ ] Create a predictions system
- [ ] Add user authentication with Firebase
- [ ] Build a backend with Node.js + Express
- [ ] Store data in a database (MongoDB/PostgreSQL)

## 🤝 Contributing

This is an open educational project! Feel free to:
- Fork the repository
- Add new features
- Improve the design
- Fix bugs
- Share your customizations

## 📄 License

This project is open source and available for educational purposes. Feel free to use, modify, and share!

## 💬 Support

Questions or need help?
- Check the code comments in `index.html`
- Review the `CLAUDE.md` file for detailed documentation
- Open an issue on GitHub
- Ask your AI assistant for guidance!

## 🎉 Credits

Created as an educational project to demonstrate modern web development techniques using only vanilla HTML, CSS, and JavaScript.

---

**Enjoy building with Pronostici Calcio!** ⚽✨
