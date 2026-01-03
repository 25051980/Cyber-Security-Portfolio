# 🌐 Web Application Documentation

## 📱 Responsiveness

This web application is built with a **mobile-first** approach and adapts gracefully to different screen sizes:

- Uses media queries to adjust layout based on screen width.
- Applies **flexbox** and **CSS grid** for flexible and responsive layout structures.
- On small screens, icons replace long text labels to optimize space without compromising usability.

---

## 🔐 Security & Admin Panel Path

> 🔧 **To be implemented**

The admin panel will be moved to a **non-obvious, protected path**, such as:


This makes it harder for unauthorized users to access the panel through direct URL guessing. In the future, access control will be enhanced with proper authentication.

---

## 🔑 Mock Login with Local Storage

- The current login system is **mocked** and uses `localStorage` to store session data.
- This allows users to stay logged in even after refreshing the page.
- **Suggested improvement:** Use `sessionStorage` to clear login state when the browser is closed, increasing security.
- **Industry standard:** Connect the login process to a **real database** with proper authentication and session handling on the server side.

---

## 📁 Project Structure & Reusability

The project is organized for better **maintainability**, **scalability**, and **code reuse**:

