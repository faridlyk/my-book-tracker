const URL = window.location.href.replace(/^https?:\/\//, '');;

document.getElementById('site-url').innerHTML = `<h1>${URL}</h1>`;
