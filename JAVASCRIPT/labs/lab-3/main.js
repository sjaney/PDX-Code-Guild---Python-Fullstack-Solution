let user = prompt("Enter a number you would like to convert into a phrase")


let ones_digit = {
    0: 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10: 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    14 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    16 : 'eighteen',
    19 : 'nineteen',
}


let tens_digit = {
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

let tens_unit = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}


if (user < 20) {
    alert(ones_digit[user])
} else if (user <= 99){
    if (user % 10 === 0){
    alert(tens_digit[user])
}
    else{
    tens = tens_unit[Math.floor(user / 10)]
    ones = ones_digit[user % 10]
    alert(tens + "-" + ones)
    }
}