  
function toggleMenu() {
    if (document.getElementById("main-nav").style.height == "0px") {
        var numChildren = document.getElementById("main-nav").childNodes.length;
        var heightFactor = window.getComputedStyle(document.body).getPropertyValue('--height-factor');
        document.getElementById("main-nav").style.height = ((numChildren) * heightFactor) + "em";
        // document.getElementById("main-nav").style.height = "100vh";
        document.getElementById("burger").classList.add("open");
    } else {
        document.getElementById("main-nav").style.height = "0px";
        document.getElementById("burger").classList.remove("open");
    }
}

  
function toggleCart() {
    if (document.getElementById("cart-content").style.display == "none") {
        document.getElementById("cart-content").style.display = "block";
    } else {
        document.getElementById("cart-content").style.display = "none";
    }
}