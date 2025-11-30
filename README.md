# 📰 NewsHub | Next-Gen News Aggregator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=for-the-badge&logo=flask&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-Animation-green?style=for-the-badge&logo=greensock&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> A high-performance, visually immersive news aggregator designed to transform how users consume information. Built with a focus on modern UI/UX principles, performance optimization, and seamless API integration.

---

## 🚀 Overview

**NewsHub** is not just another news app; it's a demonstration of modern web engineering and design capabilities. By leveraging **Flask** for a robust backend and **GSAP** for cinema-grade animations, this project delivers a "Midnight Glass" aesthetic that feels premium and responsive.

The goal was to create a "billion-dollar" user experience that prioritizes readability, visual hierarchy, and performance.

## ✨ Key Features

*   **🎨 Midnight Glass Design System**: A custom-built dark mode aesthetic featuring glassmorphism, neon accents, and dynamic gradients.
*   **⚡ High-Performance Animations**: Integrated **GSAP (GreenSock)** for scroll-triggered reveals and smooth micro-interactions (60fps).
*   **🔄 Dynamic Content Loading**: Implemented a custom JSON API endpoint to support "Load More" functionality without page reloads (AJAX-like experience).
*   **📱 Fully Responsive**: A mobile-first approach ensuring a flawless experience across desktops, tablets, and smartphones.
*   **🧠 Smart UX Details**:
    *   **Reading Time Estimates**: Automatically calculated based on article length.
    *   **Native Share API**: Integrates with the device's native sharing menu.
    *   **Lazy Loading**: Optimized image delivery for faster initial page loads.

## 🛠️ Tech Stack

### Backend
*   **Python**: Core logic and data processing.
*   **Flask**: Lightweight WSGI web application framework.
*   **Requests**: Robust HTTP library for API communication.

### Frontend
*   **HTML5 / CSS3**: Semantic markup and modern CSS (Flexbox, Grid, Variables).
*   **JavaScript (ES6+)**: Client-side logic and DOM manipulation.
*   **GSAP**: Advanced animation library for complex motion.
*   **FontAwesome**: Vector icons.

### External Services
*   **NewsAPI**: Real-time global news data source.

## 📸 Screenshots

*(Add your screenshots here. Pro Tip: Use a tool like Screely or shots.so for professional mockups)*

## 🔧 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/mohammed-aaqieb/Newshub.git
    cd Newshub
    ```

2.  **Set up a virtual environment (Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key**
    *   Get a free API key from [NewsAPI.org](https://newsapi.org/).
    *   Open `app.py` and replace `NEWS_API_KEY` with your key.

5.  **Run the application**
    ```bash
    python app.py
    ```
    Visit `http://127.0.0.1:5005` in your browser.

## 💡 Code Highlights

**Efficient Error Handling**:
The backend implements robust error catching to ensure the application never crashes, even if the external API is down.

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get('articles', [])
except requests.exceptions.RequestException as e:
    print(f"Error fetching news: {e}")
    return []
```

**Smooth Scroll Animations**:
Using GSAP ScrollTrigger to create an immersive "reveal" effect as the user scrolls.

```javascript
gsap.utils.toArray('.scroll-reveal').forEach((elem, i) => {
    gsap.from(elem, {
        scrollTrigger: { trigger: elem, start: "top 85%" },
        y: 50, opacity: 0, duration: 0.8, ease: "power3.out"
    });
});
```

License
This project is open source and available under the MIT License.

---
*Built with ❤️ and Python.*
