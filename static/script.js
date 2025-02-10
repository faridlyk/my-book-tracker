const URL = window.location.href.replace(/^https?:\/\//, '')
const API = "https://mybooktracker.vercel.app/"

const booksCont = document.querySelector("#books-cont")

document.getElementById('site-url').innerHTML = `<h1>${URL}</h1>`

;(async () => {
    const res = await fetch(API)
    const data = await res.json()
    addBook(data)
})();

const addBook = (data) => {
    for (let i = 0; i < data.length; i++) {
        if (data[i].sessions[0].end) {
            const li = document.createElement("li")
            li.classList.add("book")
            li.innerHTML = `<p>${data[i].title} by ${authorsString(data[i].authors)}</p>`
            booksCont.append(li)
        }
    }
}

const authorsString = (authorList) => {
    let returnString = authorList[0]
    if (authorList.length > 1) {
        for (let i = 0; i < authorList.length; i++) {
            if (i + 2 < authorList.length) {
                returnString += ", " + authorList[i]
            } else {
                returnString += " and " + authorList[i]
            }
        }
    }
    return returnString
}