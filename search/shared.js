const menu_btn = document.querySelector('#nav-collapse button');
const nav_items = document.querySelector('.nav-items');

menu_btn.addEventListener('click', () => {
    if (nav_items.classList.contains('nav-items-open')) {
        menu_btn.children[0].classList.remove('bi-x');
        menu_btn.children[0].classList.add('bi-list');
        nav_items.classList.remove('nav-items-open');
        return;
    }
    menu_btn.children[0].classList.remove('bi-list');
    menu_btn.children[0].classList.add('bi-x');
    nav_items.classList.add('nav-items-open');
})