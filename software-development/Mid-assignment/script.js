// script.js

// DOM elements
const productListEl    = document.getElementById("product-list");
const categoryFilterEl = document.getElementById("categoryFilter");
const sortSelectEl     = document.getElementById("sortSelect");

// Load products from localStorage or empty array
function loadProducts() {
  const productsJSON = localStorage.getItem("products");
  return productsJSON ? JSON.parse(productsJSON) : [];
}

// Render products as cards
function renderProducts(products) {
  if (!Array.isArray(products) || products.length === 0) {
    productListEl.innerHTML = `<p>No products available.</p>`;
    return;
  }

  productListEl.innerHTML = ""; // Clear

  products.forEach(product => {
    const card = document.createElement("div");
    card.className = "product-card";
    card.innerHTML = `
      <img src="${product.image}" alt="${product.name}" class="product-image" />
      <h3 class="product-name">${product.name}</h3>
      <p class="product-description">${product.description}</p>
      <p class="product-price">$${parseFloat(product.price).toFixed(2)}</p>
      <p class="product-category">Category: ${product.category}</p>
      <p class="product-availability">Available: ${product.available ? "Yes" : "No"}</p>
    `;
    productListEl.appendChild(card);
  });
}

// Populate category filter dropdown with unique categories (once)
function populateCategoryFilter(products) {
  const categories = Array.from(new Set(products.map(p => p.category))).filter(Boolean);
  categoryFilterEl.innerHTML = `<option value="all">All</option>`;
  categories.forEach(cat => {
    const opt = document.createElement("option");
    opt.value = cat;
    opt.textContent = cat;
    categoryFilterEl.appendChild(opt);
  });
}

// Filter products by category
function filterByCategory(products, category) {
  return category === "all"
    ? products
    : products.filter(p => p.category === category);
}

// Sort products based on selected option
function sortProducts(products, sortOption) {
  const sorted = [...products];
  // console.log("Sorting by:", sortOption);

  switch (sortOption) {
    case "name-asc":
      sorted.sort((a, b) => a.name.localeCompare(b.name));
      break;
    case "name-desc":
      sorted.sort((a, b) => b.name.localeCompare(a.name));
      break;
    case "price-asc":
      sorted.sort((a, b) => parseFloat(a.price) - parseFloat(b.price));
      break;
    case "price-desc":
      sorted.sort((a, b) => parseFloat(b.price) - parseFloat(a.price));
      break;
    default:
      // no-op
      break;
  }

  return sorted;
}

// Main update function, called on filter/sort change
function updateProductList() {
  const allProducts     = loadProducts();
  const selectedCategory = categoryFilterEl.value;
  const selectedSort     = sortSelectEl.value;

  // Apply category then sort
  const filtered = filterByCategory(allProducts, selectedCategory);
  const sorted   = sortProducts(filtered, selectedSort);

  renderProducts(sorted);
}

// Initialize on page load
function initialize() {
  const products = loadProducts();
  populateCategoryFilter(products);

  // Set up event listeners
  categoryFilterEl.addEventListener("change", updateProductList);
  sortSelectEl.addEventListener("change",     updateProductList);

  // Initial render
  updateProductList();
}

// Kick off
initialize();
