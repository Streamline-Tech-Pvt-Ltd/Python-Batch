// =====================================================
// GIFTORA - MAIN JAVASCRIPT
// Homepage | Shop | Search | Cart | Wishlist
// Gift Finder | Checkout | Product Details
// =====================================================


// =====================================================
// 1. COMMON HELPER FUNCTIONS
// =====================================================

function getGiftoraDiscount(button) {
    const offerCard = button
        ? button.closest(".offer-product-card")
        : null;

    if (!offerCard) {
        return 0;
    }

    const productId = Number(button.dataset.id);

    const discounts = {
        1: 20,
        2: 30,
        3: 20,
        4: 30
    };

    return discounts[productId] || 0;
}


function calculateGiftoraPrice(originalPrice, discountPercent) {
    const price = Number(originalPrice) || 0;
    const discount = Number(discountPercent) || 0;

    return Math.round(price * (100 - discount) / 100);
}


function formatGiftoraPrice(amount) {
    return "₹" + (Number(amount) || 0).toLocaleString("en-IN", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}


function getGiftoraDiscountPercent(item) {
    return Number(item.discountPercent) || 0;
}


function getGiftoraOriginalPrice(item) {
    return Number(item.originalPrice) || Number(item.price) || 0;
}


function getGiftoraCartItemPrice(item) {
    return Number(item.price) || 0;
}


function getGiftoraCart() {
    try {
        const cart = JSON.parse(
            localStorage.getItem("giftoraCart")
        );

        return Array.isArray(cart) ? cart : [];
    } catch (error) {
        console.error("Unable to read cart:", error);
        return [];
    }
}


function saveGiftoraCart(cart) {
    localStorage.setItem("giftoraCart", JSON.stringify(cart));
}


function getGiftoraProduct(productId) {
    if (typeof products === "undefined" || !Array.isArray(products)) {
        return null;
    }

    return products.find(function (product) {
        return Number(product.id) === Number(productId);
    }) || null;
}


function getGiftoraProductText(value) {
    return String(value || "");
}


// =====================================================
// 2. PRODUCT IMAGE HELPER
// Supports image paths and emoji products
// =====================================================

function getGiftoraImage(imagePath, altText = "Gift product", className = "giftora-product-image") {

    const path = String(imagePath || "").trim();

    if (!path) {
        return '<div class="giftora-image-fallback">🎁</div>';
    }

    // Emoji-only products are displayed as emoji.
    // Image paths such as ../images/cute teddy bear.jpg
    // are displayed using an actual HTML image element.

    const isImagePath =
        /\.(jpg|jpeg|png|webp|gif|svg|avif)(\?.*)?$/i.test(path);

    if (isImagePath) {
        const safePath = path
            .replace(/&/g, "&amp;")
            .replace(/"/g, "&quot;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");

        const safeAlt = String(altText)
            .replace(/&/g, "&amp;")
            .replace(/"/g, "&quot;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");

        return `
            <img
                src="${safePath}"
                alt="${safeAlt}"
                class="${className}"
                loading="lazy"
                onerror="this.onerror=null; this.style.display='none'; this.nextElementSibling.style.display='flex';"
            >
            <div class="giftora-image-fallback" style="display:none;">
                🎁
            </div>
        `;
    }

    return `
        <div class="giftora-image-fallback">
            ${path}
        </div>
    `;
}


// =====================================================
// 3. ADD PRODUCT TO CART
// =====================================================

function addGiftoraProductToCart(productId, discountPercent = 0) {

    const product = getGiftoraProduct(productId);

    if (!product) {
        alert("Sorry! Product not found.");
        return;
    }

    const originalPrice = Number(product.price) || 0;

    const finalPrice = discountPercent > 0
        ? calculateGiftoraPrice(originalPrice, discountPercent)
        : originalPrice;

    const cart = getGiftoraCart();

    const existingItem = cart.find(function (item) {
        return Number(item.id) === Number(product.id) &&
            getGiftoraDiscountPercent(item) === discountPercent;
    });

    if (existingItem) {
        existingItem.quantity =
            (Number(existingItem.quantity) || 1) + 1;
    } else {
        cart.push({
            id: product.id,
            name: product.name,
            price: finalPrice,
            originalPrice: originalPrice,
            discountPercent: discountPercent,
            image: product.image,
            quantity: 1
        });
    }

    saveGiftoraCart(cart);

    updateGiftoraCartCount();

    alert(product.name + " added to your cart! 🛒");
}


// =====================================================
// 4. UPDATE CART COUNT
// =====================================================

function updateGiftoraCartCount() {

    const cart = getGiftoraCart();

    const totalQuantity = cart.reduce(function (total, item) {
        return total + (Number(item.quantity) || 1);
    }, 0);

    document.querySelectorAll(
        "#cartCount, #cart-count, .cart-count"
    ).forEach(function (element) {
        element.textContent = totalQuantity;
    });
}


// =====================================================
// 5. HOMEPAGE AND SHOP PRODUCT CARDS
// =====================================================

function renderGiftoraProducts(productList, container) {

    if (!container) {
        return;
    }

    if (!Array.isArray(productList) || productList.length === 0) {
        container.innerHTML = `
            <div class="col-12 text-center py-5">
                <h3 class="h5">No gifts found.</h3>
                <p class="text-muted">
                    Try another search or select a different category.
                </p>
            </div>
        `;
        return;
    }

    container.innerHTML = productList.map(function (product) {

        return `
            <div class="col-12 col-sm-6 col-lg-4">
                <article class="card product-card h-100 border-0 shadow-sm rounded-4">

                    <div class="giftora-product-image-container">
                        ${getGiftoraImage(
                            product.image,
                            product.name,
                            "product-image"
                        )}
                    </div>

                    <div class="card-body p-4 text-center">

                        <span class="badge text-bg-primary mb-3">
                            ${getGiftoraProductText(product.category)}
                        </span>

                        <h3 class="h5 fw-bold">
                            ${getGiftoraProductText(product.name)}
                        </h3>

                        <p class="text-muted">
                            ${getGiftoraProductText(product.description)}
                        </p>

                        <p class="fw-bold fs-5">
                            ${formatGiftoraPrice(product.price)}
                        </p>

                        <p class="text-warning">
                            ★ ${Number(product.rating) || 0} / 5
                        </p>

                        <div class="d-flex justify-content-center gap-2 flex-wrap">

                            <button
                                type="button"
                                class="btn btn-primary add-to-cart"
                                data-id="${product.id}">
                                🛒 Add to Cart
                            </button>

                            <button
                                type="button"
                                class="btn btn-outline-danger add-to-wishlist"
                                data-id="${product.id}">
                                ♡ Wishlist
                            </button>

                        </div>

                        <button
                            type="button"
                            class="btn btn-link view-details-btn mt-2"
                            data-id="${product.id}">
                            View Details
                        </button>

                    </div>
                </article>
            </div>
        `;

    }).join("");
}


// =====================================================
// 6. SHOP SEARCH, FILTER AND SORT
// =====================================================

function initializeGiftoraShop() {

    const shopProducts = document.getElementById("shopProducts");

    if (!shopProducts) {
        return;
    }

    const searchInput = document.getElementById("searchInput");
    const categoryFilter = document.getElementById("categoryFilter");
    const sortFilter = document.getElementById("sortFilter");
    const productCount = document.getElementById("productCount");

    function filterProducts() {

        const searchText = searchInput
            ? searchInput.value.trim().toLowerCase()
            : "";

        const selectedCategory = categoryFilter
            ? categoryFilter.value
            : "all";

        let filteredProducts = products.filter(function (product) {

            const searchableText = [
                product.name,
                product.description,
                product.category,
                product.occasion,
                product.recipient
            ].map(function (value) {
                return getGiftoraProductText(value).toLowerCase();
            }).join(" ");

            const matchesSearch = searchableText.includes(searchText);

            const matchesCategory =
                selectedCategory === "all" ||
                product.category === selectedCategory;

            return matchesSearch && matchesCategory;
        });

        const sortValue = sortFilter
            ? sortFilter.value
            : "default";

        switch (sortValue) {

            case "price-low":
                filteredProducts.sort(function (a, b) {
                    return Number(a.price) - Number(b.price);
                });
                break;

            case "price-high":
                filteredProducts.sort(function (a, b) {
                    return Number(b.price) - Number(a.price);
                });
                break;

            case "name-az":
                filteredProducts.sort(function (a, b) {
                    return a.name.localeCompare(b.name);
                });
                break;

            case "rating-high":
                filteredProducts.sort(function (a, b) {
                    return Number(b.rating) - Number(a.rating);
                });
                break;
        }

        renderGiftoraProducts(filteredProducts, shopProducts);

        if (productCount) {
            productCount.textContent =
                filteredProducts.length +
                (filteredProducts.length === 1
                    ? " product"
                    : " products");
        }
    }

    filterProducts();

    if (searchInput) {
        searchInput.addEventListener("input", filterProducts);
    }

    if (categoryFilter) {
        categoryFilter.addEventListener("change", filterProducts);
    }

    if (sortFilter) {
        sortFilter.addEventListener("change", filterProducts);
    }
}


// =====================================================
// 7. CART DISPLAY AND QUANTITY MANAGEMENT
// =====================================================

function initializeGiftoraCart() {

    const cartItemsContainer = document.getElementById("cartItems");

    if (!cartItemsContainer) {
        return;
    }

    const totalItemsElement = document.getElementById("totalItems");
    const totalAmountElement = document.getElementById("totalAmount");

    function displayCartItems() {

        const cart = getGiftoraCart();

        cartItemsContainer.innerHTML = "";

        let totalItems = 0;
        let totalAmount = 0;

        if (cart.length === 0) {

            cartItemsContainer.innerHTML = `
                <div class="text-center p-5">
                    <h3>🛒 Your Cart is Empty!</h3>

                    <p class="text-muted">
                        Find the perfect gift for someone special.
                    </p>

                    <a href="shop.html" class="btn btn-primary mt-3">
                        Explore Gifts
                    </a>
                </div>
            `;

        } else {

            cart.forEach(function (item) {

                const quantity = Number(item.quantity) || 1;
                const price = getGiftoraCartItemPrice(item);
                const originalPrice = getGiftoraOriginalPrice(item);
                const discountPercent = getGiftoraDiscountPercent(item);

                const itemTotal = price * quantity;
                const originalTotal = originalPrice * quantity;

                const savings = Math.max(0, originalTotal - itemTotal);

                totalItems += quantity;
                totalAmount += itemTotal;

                const card = document.createElement("div");

                card.className =
                    "card mb-3 p-3 shadow-sm rounded-4";

                card.innerHTML = `
                    <div class="d-flex align-items-center gap-3 flex-wrap">

                        <div class="cart-product-image-container">
                            ${getGiftoraImage(
                                item.image,
                                item.name,
                                "cart-product-image"
                            )}
                        </div>

                        <div class="flex-grow-1">

                            <h5>
                                ${getGiftoraProductText(item.name)}
                            </h5>

                            <p class="mb-1">
                                Price:

                                ${
                                    discountPercent > 0
                                        ? `
                                            <del class="text-muted">
                                                ${formatGiftoraPrice(originalPrice)}
                                            </del>

                                            <span class="text-success fw-bold">
                                                ${formatGiftoraPrice(price)}
                                            </span>

                                            <span class="badge bg-danger">
                                                ${discountPercent}% OFF
                                            </span>
                                        `
                                        : formatGiftoraPrice(price)
                                }
                            </p>

                            ${
                                savings > 0
                                    ? `
                                        <small class="text-success">
                                            You save ${formatGiftoraPrice(savings)}
                                        </small>
                                    `
                                    : ""
                            }

                            <div class="d-flex align-items-center gap-2 mt-2">

                                <button
                                    type="button"
                                    class="btn btn-sm btn-outline-secondary decrease-quantity"
                                    data-id="${item.id}"
                                    data-discount="${discountPercent}">
                                    −
                                </button>

                                <span class="fw-bold">
                                    ${quantity}
                                </span>

                                <button
                                    type="button"
                                    class="btn btn-sm btn-outline-secondary increase-quantity"
                                    data-id="${item.id}"
                                    data-discount="${discountPercent}">
                                    +
                                </button>

                            </div>

                            <button
                                type="button"
                                class="btn btn-sm btn-outline-danger remove-product mt-2"
                                data-id="${item.id}"
                                data-discount="${discountPercent}">
                                🗑️ Remove
                            </button>

                        </div>

                        <strong>
                            ${formatGiftoraPrice(itemTotal)}
                        </strong>

                    </div>
                `;

                cartItemsContainer.appendChild(card);
            });
        }

        if (totalItemsElement) {
            totalItemsElement.textContent = totalItems;
        }

        if (totalAmountElement) {
            totalAmountElement.textContent =
                formatGiftoraPrice(totalAmount);
        }

        updateGiftoraCartCount();
    }

    cartItemsContainer.addEventListener("click", function (event) {

        const increaseButton =
            event.target.closest(".increase-quantity");

        const decreaseButton =
            event.target.closest(".decrease-quantity");

        const removeButton =
            event.target.closest(".remove-product");

        if (!increaseButton && !decreaseButton && !removeButton) {
            return;
        }

        const clickedButton =
            increaseButton || decreaseButton || removeButton;

        const productId = Number(clickedButton.dataset.id);

        const discountPercent =
            Number(clickedButton.dataset.discount) || 0;

        const cart = getGiftoraCart();

        const productIndex = cart.findIndex(function (item) {
            return Number(item.id) === productId &&
                getGiftoraDiscountPercent(item) === discountPercent;
        });

        if (productIndex === -1) {
            return;
        }

        if (increaseButton) {

            cart[productIndex].quantity =
                (Number(cart[productIndex].quantity) || 1) + 1;

        } else if (decreaseButton) {

            cart[productIndex].quantity =
                (Number(cart[productIndex].quantity) || 1) - 1;

            if (cart[productIndex].quantity <= 0) {
                cart.splice(productIndex, 1);
            }

        } else if (removeButton) {

            cart.splice(productIndex, 1);
        }

        saveGiftoraCart(cart);

        displayCartItems();
    });

    displayCartItems();
}


// =====================================================
// 8. CHECKOUT BUTTON
// =====================================================

function initializeGiftoraCheckoutButton() {

    const checkoutBtn = document.getElementById("checkoutBtn");

    if (!checkoutBtn) {
        return;
    }

    checkoutBtn.addEventListener("click", function (event) {

        const cart = getGiftoraCart();

        if (cart.length === 0) {
            event.preventDefault();

            alert(
                "Your cart is empty! Please add some gifts first."
            );

            return;
        }

        window.location.href = "checkout.html";
    });
}


// =====================================================
// 9. CHECKOUT ORDER SUMMARY
// =====================================================

function initializeGiftoraCheckoutSummary() {

    const checkoutItems = document.getElementById("checkoutItems");

    if (!checkoutItems) {
        return;
    }

    const checkoutTotalItems =
        document.getElementById("checkoutTotalItems");

    const checkoutTotalAmount =
        document.getElementById("checkoutTotalAmount");

    const cart = getGiftoraCart();

    checkoutItems.innerHTML = "";

    if (cart.length === 0) {

        checkoutItems.innerHTML = `
            <p class="text-muted">Your cart is empty.</p>

            <a href="shop.html" class="btn btn-primary">
                Explore Gifts
            </a>
        `;

        if (checkoutTotalItems) {
            checkoutTotalItems.textContent = "0";
        }

        if (checkoutTotalAmount) {
            checkoutTotalAmount.textContent = formatGiftoraPrice(0);
        }

        return;
    }

    let totalItems = 0;
    let totalAmount = 0;
    let totalSavings = 0;

    cart.forEach(function (item) {

        const quantity = Number(item.quantity) || 1;
        const price = getGiftoraCartItemPrice(item);
        const originalPrice = getGiftoraOriginalPrice(item);
        const discountPercent = getGiftoraDiscountPercent(item);

        const lineTotal = price * quantity;

        const savings = Math.max(
            0,
            (originalPrice - price) * quantity
        );

        totalItems += quantity;
        totalAmount += lineTotal;
        totalSavings += savings;

        const productRow = document.createElement("div");

        productRow.className =
            "d-flex justify-content-between align-items-start mb-3 gap-3";

        const productName = document.createElement("span");

        productName.textContent =
            getGiftoraProductText(item.name) + " × " + quantity;

        if (discountPercent > 0) {

            const discountLabel = document.createElement("small");

            discountLabel.className = "text-success d-block";

            discountLabel.textContent =
                discountPercent + "% OFF";

            productName.appendChild(document.createElement("br"));

            productName.appendChild(discountLabel);
        }

        const productPrice = document.createElement("div");

        productPrice.className = "text-end";

        if (discountPercent > 0) {

            productPrice.innerHTML = `
                <del class="text-muted small">
                    ${formatGiftoraPrice(originalPrice * quantity)}
                </del>

                <br>

                <strong class="text-success">
                    ${formatGiftoraPrice(lineTotal)}
                </strong>
            `;

        } else {

            productPrice.innerHTML = `
                <strong>${formatGiftoraPrice(lineTotal)}</strong>
            `;
        }

        productRow.appendChild(productName);
        productRow.appendChild(productPrice);

        checkoutItems.appendChild(productRow);
    });

    let savingsElement =
        document.getElementById("checkoutTotalSavings");

    if (!savingsElement) {

        savingsElement = document.createElement("p");

        savingsElement.id = "checkoutTotalSavings";

        savingsElement.className = "text-success fw-semibold";

        if (checkoutTotalAmount && checkoutTotalAmount.parentElement) {

            checkoutTotalAmount.parentElement.insertAdjacentElement(
                "beforebegin",
                savingsElement
            );

        } else {

            checkoutItems.insertAdjacentElement(
                "afterend",
                savingsElement
            );
        }
    }

    savingsElement.textContent = totalSavings > 0
        ? "You save " + formatGiftoraPrice(totalSavings) + " with offers!"
        : "";

    if (checkoutTotalItems) {
        checkoutTotalItems.textContent = totalItems;
    }

    if (checkoutTotalAmount) {
        checkoutTotalAmount.textContent =
            formatGiftoraPrice(totalAmount);
    }
}


// =====================================================
// 10. PLACE ORDER
// =====================================================

function initializeGiftoraPlaceOrder() {

    const checkoutForm = document.getElementById("checkoutForm");

    if (!checkoutForm) {
        return;
    }

    checkoutForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const cart = getGiftoraCart();

        if (cart.length === 0) {

            alert(
                "Your cart is empty! Please add some gifts first."
            );

            window.location.href = "shop.html";

            return;
        }

        const customerName =
            document.getElementById("customerName")?.value.trim() || "";

        const customerEmail =
            document.getElementById("customerEmail")?.value.trim() || "";

        const customerPhone =
            document.getElementById("customerPhone")?.value.trim() || "";

        const customerAddress =
            document.getElementById("customerAddress")?.value.trim() || "";

        const customerCity =
            document.getElementById("customerCity")?.value.trim() || "";

        const customerPincode =
            document.getElementById("customerPincode")?.value.trim() || "";

        let totalItems = 0;
        let totalAmount = 0;
        let totalSavings = 0;

        cart.forEach(function (item) {

            const quantity = Number(item.quantity) || 1;
            const price = getGiftoraCartItemPrice(item);
            const originalPrice = getGiftoraOriginalPrice(item);

            totalItems += quantity;
            totalAmount += price * quantity;

            totalSavings += Math.max(
                0,
                originalPrice - price
            ) * quantity;
        });

        const order = {
            orderId: "GFT" + Date.now(),

            customer: {
                name: customerName,
                email: customerEmail,
                phone: customerPhone,
                address: customerAddress,
                city: customerCity,
                pincode: customerPincode
            },

            items: cart,
            totalItems: totalItems,
            totalAmount: totalAmount,
            totalSavings: totalSavings,
            orderDate: new Date().toLocaleString("en-IN"),
            status: "Confirmed"
        };

        let orders = [];

        try {

            const savedOrders = JSON.parse(
                localStorage.getItem("giftoraOrders")
            );

            orders = Array.isArray(savedOrders)
                ? savedOrders
                : [];

        } catch (error) {

            orders = [];
        }

        orders.push(order);

        localStorage.setItem(
            "giftoraOrders",
            JSON.stringify(orders)
        );

        localStorage.removeItem("giftoraCart");

        updateGiftoraCartCount();

        alert(
            "🎉 Order Placed Successfully!\n\n" +
            "Order ID: " + order.orderId + "\n" +
            "Customer: " + customerName + "\n" +
            "Total Items: " + totalItems + "\n" +
            "Total Amount: " + formatGiftoraPrice(totalAmount) + "\n" +
            (
                totalSavings > 0
                    ? "You Saved: " + formatGiftoraPrice(totalSavings) + "\n\n"
                    : "\n"
            ) +
            "Thank you for shopping with Giftora! ❤️"
        );

        window.location.href = "index.html";
    });
}


// =====================================================
// 11. WISHLIST
// =====================================================

function initializeGiftoraWishlist() {

    const wishlistContainer =
        document.getElementById("wishlistItems");

    const emptyWishlist =
        document.getElementById("emptyWishlist");

    const wishlistCount =
        document.getElementById("wishlistCount");

    function getWishlist() {

        try {

            const wishlist = JSON.parse(
                localStorage.getItem("giftoraWishlist")
            );

            return Array.isArray(wishlist) ? wishlist : [];

        } catch (error) {

            return [];
        }
    }

    function saveWishlist(wishlist) {

        localStorage.setItem(
            "giftoraWishlist",
            JSON.stringify(wishlist)
        );
    }

    function displayWishlist() {

        if (!wishlistContainer) {
            return;
        }

        const wishlist = getWishlist();

        wishlistContainer.innerHTML = "";

        if (wishlistCount) {

            wishlistCount.textContent =
                wishlist.length +
                (wishlist.length === 1
                    ? " Saved Gift"
                    : " Saved Gifts");
        }

        if (wishlist.length === 0) {

            if (emptyWishlist) {
                emptyWishlist.classList.remove("d-none");
            }

            wishlistContainer.innerHTML = `
                <div class="col-12 text-center py-4">

                    <p class="text-muted">
                        Your wishlist is empty.
                    </p>

                    <a href="shop.html" class="btn btn-primary">
                        Explore Gifts
                    </a>

                </div>
            `;

            return;
        }

        if (emptyWishlist) {
            emptyWishlist.classList.add("d-none");
        }

        wishlist.forEach(function (item) {

            const product = getGiftoraProduct(item.id);

            if (!product) {
                return;
            }

            const card = document.createElement("div");

            card.className = "col-12 col-sm-6 col-lg-4";

            card.innerHTML = `
                <div class="wishlist-card">

                    <div class="wishlist-image">
                        ${getGiftoraImage(
                            product.image,
                            product.name,
                            "wishlist-product-image"
                        )}
                    </div>

                    <div class="card-body">

                        <span class="badge bg-primary mb-2">
                            ${getGiftoraProductText(product.category)}
                        </span>

                        <h5 class="fw-bold">
                            ${getGiftoraProductText(product.name)}
                        </h5>

                        <p class="text-muted small">
                            ${getGiftoraProductText(product.description)}
                        </p>

                        <p class="mb-2">
                            ⭐ ${Number(product.rating) || 0}
                        </p>

                        <p class="wishlist-price">
                            ${formatGiftoraPrice(product.price)}
                        </p>

                        <div class="d-flex gap-2 flex-wrap">

                            <button
                                type="button"
                                class="btn btn-primary flex-grow-1"
                                data-wishlist-cart="${product.id}">
                                🛒 Add to Cart
                            </button>

                            <button
                                type="button"
                                class="btn wishlist-remove"
                                data-wishlist-remove="${product.id}">
                                🗑️ Remove
                            </button>

                        </div>

                    </div>
                </div>
            `;

            wishlistContainer.appendChild(card);
        });
    }

    if (wishlistContainer) {

        wishlistContainer.addEventListener("click", function (event) {

            const removeButton =
                event.target.closest("[data-wishlist-remove]");

            const cartButton =
                event.target.closest("[data-wishlist-cart]");

            if (removeButton) {

                const productId =
                    Number(removeButton.dataset.wishlistRemove);

                const updatedWishlist = getWishlist().filter(
                    function (item) {
                        return Number(item.id) !== productId;
                    }
                );

                saveWishlist(updatedWishlist);

                displayWishlist();

                return;
            }

            if (cartButton) {

                const productId =
                    Number(cartButton.dataset.wishlistCart);

                addGiftoraProductToCart(productId, 0);
            }
        });
    }

    document.addEventListener("click", function (event) {

        const wishlistButton = event.target.closest(
            ".add-to-wishlist, [data-add-wishlist]"
        );

        if (!wishlistButton) {
            return;
        }

        const productId = Number(
            wishlistButton.dataset.id ||
            wishlistButton.dataset.addWishlist
        );

        const product = getGiftoraProduct(productId);

        if (!product) {
            return;
        }

        const wishlist = getWishlist();

        const alreadyExists = wishlist.some(function (item) {
            return Number(item.id) === productId;
        });

        if (alreadyExists) {

            alert("This gift is already in your wishlist! ❤️");

            return;
        }

        wishlist.push({
            id: product.id
        });

        saveWishlist(wishlist);

        alert(product.name + " added to your wishlist! ❤️");

        displayWishlist();
    });

    displayWishlist();
}


// =====================================================
// 12. SMART GIFT FINDER
// =====================================================

function initializeGiftoraGiftFinder() {

    const giftFinderForm =
        document.getElementById("giftFinderForm");

    const giftResults =
        document.getElementById("giftResults");

    const finderEmpty =
        document.getElementById("finderEmpty");

    if (!giftFinderForm || !giftResults) {
        return;
    }

    giftFinderForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const recipient =
            document.getElementById("recipient")?.value || "";

        const occasion =
            document.getElementById("occasion")?.value || "";

        const budget =
            Number(document.getElementById("budget")?.value) || 0;

        const category =
            document.getElementById("giftCategory")?.value || "all";

        const filteredProducts = products.filter(function (product) {

            const matchesRecipient =
                product.recipient === recipient;

            const matchesOccasion =
                product.occasion === occasion;

            const matchesBudget =
                Number(product.price) <= budget;

            const matchesCategory =
                category === "all" ||
                product.category === category;

            return matchesRecipient &&
                matchesOccasion &&
                matchesBudget &&
                matchesCategory;
        });

        giftResults.innerHTML = "";

        if (finderEmpty) {
            finderEmpty.classList.add("d-none");
        }

        if (filteredProducts.length === 0) {

            giftResults.innerHTML = `
                <div class="col-12 text-center py-5">

                    <div style="font-size:4rem;">
                        💝
                    </div>

                    <h3 class="mt-3">
                        No Matching Gifts Found
                    </h3>

                    <p class="text-muted">
                        Try changing your recipient, occasion, or budget.
                    </p>

                </div>
            `;

            return;
        }

        filteredProducts.forEach(function (product) {

            const card = document.createElement("div");

            card.className = "col-12 col-sm-6 col-lg-4";

            card.innerHTML = `
                <article class="card gift-product-card h-100 border-0 shadow-sm rounded-4">

                    <div class="gift-product-image">
                        ${getGiftoraImage(
                            product.image,
                            product.name,
                            "gift-finder-product-image"
                        )}
                    </div>

                    <div class="card-body">

                        <span class="gift-category">
                            ${getGiftoraProductText(product.category)}
                        </span>

                        <h3 class="card-title">
                            ${getGiftoraProductText(product.name)}
                        </h3>

                        <p class="gift-product-description">
                            ${getGiftoraProductText(product.description)}
                        </p>

                        <p class="gift-rating">
                            ⭐ ${Number(product.rating) || 0} / 5
                        </p>

                        <p class="gift-price">
                            ${formatGiftoraPrice(product.price)}
                        </p>

                        <div class="d-grid gap-2 mt-auto">

                            <button
                                type="button"
                                class="btn btn-primary add-to-cart"
                                data-id="${product.id}">
                                🛒 Add to Cart
                            </button>

                            <button
                                type="button"
                                class="btn btn-outline-danger add-to-wishlist"
                                data-id="${product.id}">
                                ❤️ Add to Wishlist
                            </button>

                            <button
                                type="button"
                                class="btn btn-link view-details-btn"
                                data-id="${product.id}">
                                View Details
                            </button>

                        </div>

                    </div>
                </article>
            `;

            giftResults.appendChild(card);
        });
    });
}


// =====================================================
// 13. PRODUCT DETAILS
// =====================================================

function initializeGiftoraProductDetails() {

    document.addEventListener("click", function (event) {

        const button = event.target.closest(".view-details-btn");

        if (!button) {
            return;
        }

        const productId = Number(button.dataset.id);

        const product = getGiftoraProduct(productId);

        if (!product) {
            return;
        }

        const detailsContent =
            document.getElementById("productDetailsContent");

        const modalElement =
            document.getElementById("productDetailsModal");

        if (!detailsContent || !modalElement) {

            alert(
                product.name + "\n\n" +
                product.description + "\n\n" +
                "Price: " + formatGiftoraPrice(product.price)
            );

            return;
        }

        detailsContent.innerHTML = `
            <div class="text-center mb-3">

                <div class="giftora-details-image-container">
                    ${getGiftoraImage(
                        product.image,
                        product.name,
                        "details-product-image"
                    )}
                </div>

                <h4 class="fw-bold mt-2">
                    ${getGiftoraProductText(product.name)}
                </h4>

                <h5 class="text-primary fw-bold">
                    ${formatGiftoraPrice(product.price)}
                </h5>

                <p class="text-warning mb-2">
                    ⭐ ${Number(product.rating) || 0}
                </p>

            </div>

            <p>
                ${getGiftoraProductText(product.description)}
            </p>

            <p>
                <strong>Category:</strong>
                ${getGiftoraProductText(product.category)}
            </p>

            <p>
                <strong>Occasion:</strong>
                ${getGiftoraProductText(product.occasion)}
            </p>

            <p>
                <strong>Recipient:</strong>
                ${getGiftoraProductText(product.recipient)}
            </p>
        `;

        if (typeof bootstrap !== "undefined") {

            const modal = bootstrap.Modal.getOrCreateInstance(
                modalElement
            );

            modal.show();
        }
    });
}


// =====================================================
// 14. GLOBAL ADD TO CART HANDLER
// =====================================================

document.addEventListener("click", function (event) {

    const button = event.target.closest(".add-to-cart");

    if (!button) {
        return;
    }

    const productId = Number(button.dataset.id);

    const discountPercent = getGiftoraDiscount(button);

    addGiftoraProductToCart(productId, discountPercent);
});


// =====================================================
// 15. INITIALIZE ALL GIFTORA FEATURES
// =====================================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Giftora main.js loaded successfully!");

    if (typeof products === "undefined" || !Array.isArray(products)) {

        console.error(
            "Product data could not be loaded. Check products.js and its script path."
        );

        return;
    }

    // Homepage featured products
    const trendingProducts =
        document.getElementById("trendingProducts");

    if (trendingProducts) {

        const featuredProducts = products.filter(function (product) {
            return product.featured === true;
        });

        renderGiftoraProducts(featuredProducts, trendingProducts);
    }

    // Initialize all pages
    initializeGiftoraShop();

    initializeGiftoraCart();

    initializeGiftoraCheckoutButton();

    initializeGiftoraCheckoutSummary();

    initializeGiftoraPlaceOrder();

    initializeGiftoraWishlist();

    initializeGiftoraGiftFinder();

    initializeGiftoraProductDetails();

    updateGiftoraCartCount();

    console.log("Giftora features initialized successfully!");
});