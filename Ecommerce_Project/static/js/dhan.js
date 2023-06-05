let main = document.getElementById("main")
let homepage = document.getElementById("homepage")
let createdesign = document.getElementById("createdesign")
let contact = document.getElementById("contact")
let aboutus = document.getElementById("aboutus")
let  cart = document.getElementById("cart")






function homepageid(){
    main.removeChild(homepage)
    main.appendChild(createdesign)
    document.removeChild(contact)
    document.removeChild(aboutus)
    document.removeChild(cart)
};