const currentList = document.querySelector('#currentList')
const completedList = document.querySelector('#completedList')
const input = document.querySelector('#input')
const todo = input.querySelector('#todo')
const add = input.querySelector('#add')
const clear = input.querySelector('#clear')


add.addEventListener('click', todoList)



function todoList() {
    let text = todo.value 
    let div = document.createElement('div')
    let list = document.createElement('il')
    let deleteBtn = document.createElement('button')
    let checkbox = document.createElement('input')

    list.innerText = text

    checkbox.setAttribute('type', 'checkbox', 'checked')
    checkbox.addEventListener('click', function() {
        completedList.prepend(div)
    })
    
    deleteBtn.innerText = 'Delete'
    deleteBtn.addEventListener('click', function() {
        div.remove()
    })

    todo.value = ''

    div.appendChild(deleteBtn)
    div.appendChild(checkbox)
    currentList.append(div)
    div.appendChild(list)
}

