// login.js
const adminLinkContainer = document.getElementById("adminLinkContainer");
const authButtonContainer = document.getElementById("authButtonContainer");

function updateHeaderLinks() {
  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

  // Admin Panel link
  if (isLoggedIn) {
    adminLinkContainer.innerHTML = `<a href="/admin/admin.html">Admin Panel</a>`;
    authButtonContainer.innerHTML = `<a href="#" id="logoutBtn">Logout</a>`;
  } else {
    adminLinkContainer.innerHTML = ""; // hide Admin Panel
    authButtonContainer.innerHTML = `<a href="#" id="loginBtn">Login</a>`;
  }

  // Set up auth button actions
  const loginBtn = document.getElementById("loginBtn");
  const logoutBtn = document.getElementById("logoutBtn");

  if (loginBtn) {
    loginBtn.addEventListener("click", (e) => {
      e.preventDefault();
      localStorage.setItem("isLoggedIn", "true");
      updateHeaderLinks();
    });
  }

  if (logoutBtn) {
    logoutBtn.addEventListener("click", (e) => {
      e.preventDefault();
      localStorage.removeItem("isLoggedIn");
      updateHeaderLinks();
      window.location.href = "../home/index.html"; 
    });
  }
}

// Initial call to set the header links on page load
updateHeaderLinks();
