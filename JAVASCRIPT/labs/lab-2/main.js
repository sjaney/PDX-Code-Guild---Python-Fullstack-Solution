
let passLength = prompt("How many characters would you like your password to be?")

let characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()?"

let emptyStr= ''

let i = 0

while (i < passLength){
    randPass = characters[Math.floor(Math.random() * characters.length)]
    emptyStr += randPass
    i++
}

alert(`Your password is ${emptyStr}`)