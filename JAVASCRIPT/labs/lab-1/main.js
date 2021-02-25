
let user = prompt("Choose rock, paper, or scissors.")

let computer = ['rock', 'paper', 'scissors']
let randPick = computer[Math.floor(Math.random() * computer.length)]

if (randPick === 'rock' && user === 'paper'){
    alert(`Computer picks ${randPick}. You win!`)
}
else if (randPick === 'rock' && user === 'scissors'){
    alert(`Computer picks ${randPick}. You lost!`)
}
else if (randPick === 'paper' && user === 'rock'){
    alert(`Computer picks ${randPick}. You lost!`)
}
else if (randPick === 'paper' && user === 'scissors'){
    alert(`Computer picks ${randPick}. You win!`)
}
else if (randPick === 'scissors' && user === 'rock'){
    alert(`Computer picks ${randPick}. You win!`)   
}
else if (randPick === 'scissors' && user === 'paper'){
    alert(`Computer picks ${randPick}.You lose!`)
}
else{
    alert(`Computer picks ${randPick}. You tie!`)
}