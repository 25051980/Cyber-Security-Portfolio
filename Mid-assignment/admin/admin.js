// Utility: Convert File to Base64 string (returns Promise)
function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = (err) => reject(err);
    reader.readAsDataURL(file);
  });
}

// Get references to DOM elements
const form = document.getElementById("product-form");
const productListTbody = document.getElementById("admin-product-list");

// Load products from localStorage or initialize empty array
function loadProducts() {
  const productsJSON = localStorage.getItem("products");
  return productsJSON ? JSON.parse(productsJSON) : [];
}

// Save products array to localStorage
function saveProducts(products) {
  localStorage.setItem("products", JSON.stringify(products));
}

// Render product list in the table
function renderProducts() {
  const products = loadProducts();
  productListTbody.innerHTML = ""; // clear

  products.forEach((product, index) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
  <td>${product.name}</td>
  <td><img src="${product.image}" alt="${
      product.name
    }" style="width: 80px; height: auto;" /></td>
  <td>${product.description}</td>
  <td>$${parseFloat(product.price).toFixed(2)}</td>
  <td>${product.category}</td>
  <td>${product.available ? "Yes" : "No"}</td>
  <td>
    <button data-index="${index}" class="btn btn-sm btn-outline-secondary edit-btn">✏️</button>
    <button data-index="${index}" class="btn btn-sm btn-outline-danger delete-btn">❌</button>
  </td>
`;

    productListTbody.appendChild(tr);
  });
}

// Delete product handler with confirmation modal
productListTbody.addEventListener("click", async (e) => {
  if (e.target.classList.contains("delete-btn")) {
    const index = e.target.getAttribute("data-index");

    // Show confirmation modal before deleting
    const confirmed = await showConfirmModal(
      "Are you sure you want to delete this product?",
      "Delete"
    );
    if (!confirmed) {
      return; // User cancelled deletion
    }
    const products = loadProducts();
    products.splice(index, 1);
    saveProducts(products);
    renderProducts();
    // ⏳ Add delay before showing success confirmation
    await new Promise((resolve) => setTimeout(resolve, 500));
    // Show confirmation modal with OK button
    await showConfirmModal("✅ Product deleted successfully!", "OK");
  }
});


let editingIndex = null; // null means no product is being edited

productListTbody.addEventListener("click", (e) => {
  if (e.target.classList.contains("edit-btn")) {
    const index = e.target.getAttribute("data-index");
    startEditingProduct(index);
  }
});

function startEditingProduct(index) {
  const products = loadProducts();
  const product = products[index];

  // Fill the form with product data
  form.name.value = product.name;
  form.description.value = product.description;
  form.price.value = product.price;
  form.category.value = product.category;
  form.available.checked = product.available;

  // We cannot set file input programmatically (security), so no image change here

  editingIndex = index;

  // Change form submit button text to "Update Product"
  form.querySelector('button[type="submit"]').textContent = "Update Product";
}

// Create and show confirmation modal
// Added optional param confirmLabel for button text
function showConfirmModal(message, confirmLabel = "") {
  return new Promise((resolve) => {
    const modal = document.getElementById("confirm-modal");
    const modalDesc = document.getElementById("modal-desc");
    const cancelBtn = document.getElementById("cancel-btn");
    const confirmDeleteBtn = document.getElementById("confirm-delete-btn");
    const overlay = document.getElementById("modal-overlay");

    modalDesc.textContent = message;
    confirmDeleteBtn.textContent = confirmLabel;

    // Show modal and overlay
    modal.hidden = false;
    overlay.hidden = false;
    overlay.classList.add("active");

    cancelBtn.focus();

    function cleanup() {
      modal.hidden = true;
      overlay.hidden = true;
      overlay.classList.remove("active");
      cancelBtn.removeEventListener("click", onCancel);
      confirmDeleteBtn.removeEventListener("click", onConfirm);
      document.removeEventListener("keydown", onKeyDown);
    }

    function onCancel() {
      cleanup();
      resolve(false);
    }

    function onConfirm() {
      cleanup();
      resolve(true);
    }

    function onKeyDown(e) {
      if (e.key === "Escape") {
        cleanup();
        resolve(false);
      }
    }

    cancelBtn.addEventListener("click", onCancel);
    confirmDeleteBtn.addEventListener("click", onConfirm);
    document.addEventListener("keydown", onKeyDown);

    // Optional: clicking overlay cancels modal
    overlay.addEventListener("click", onCancel, { once: true });
  });
}

// Form submit handler with confirmation modal
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = form.name.value.trim();
  const description = form.description.value.trim();
  const price = form.price.value;
  const category = form.category.value;
  const available = form.available.checked;
  const imageFile = form.image.files[0];

  try {
    const products = loadProducts();

    let imageBase64;

    if (editingIndex !== null) {
      // Editing existing product

      if (imageFile) {
        // If new image selected, convert it
        imageBase64 = await fileToBase64(imageFile);
      } else {
        // Keep existing image
        imageBase64 = products[editingIndex].image;
      }

      // Update product
      products[editingIndex] = {
        name,
        description,
        price,
        category,
        available,
        image: imageBase64,
      };

      // Reset editing state before showing modal
      editingIndex = null;

      // Reset submit button text
      form.querySelector('button[type="submit"]').textContent = "Save Product";

      saveProducts(products);
      form.reset();
      renderProducts();

      // Show confirmation modal with OK button
      await showConfirmModal("✏️ Product updated successfully!", "OK");
    } else {
      // Adding new product

      if (!imageFile) {
        alert("Please select an image.");
        return;
      }

      imageBase64 = await fileToBase64(imageFile);

      const newProduct = {
        name,
        description,
        price,
        category,
        available,
        image: imageBase64,
      };

      products.push(newProduct);
      saveProducts(products);
      form.reset();
      renderProducts();

      // Show confirmation modal with OK button
      await showConfirmModal("✅ Product saved successfully!", "OK");
    }
  } catch (error) {
    alert("Error processing image file: " + error);
  }
});

// Initial render on page load
renderProducts();
