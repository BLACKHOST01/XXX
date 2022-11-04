// // // // console.log('hsdjhsfjs')
// // // // const user = document.getElementsByTagName("h1")
// // // // console.log(user)

// // // let date = new Date();
// // // year = date.getDate();
// // // month = date.getMonth();
// // // // date = date.toLocaleDateString();
// // // console.log(date,);
// // // console.log(year);
// // // console.log(month);
// // window.prompt('ajsfak');
// // console.log("asjdf");
//  const logo = document.getElementById("logo");
//  logo.style.color = "red";
 
//  console.log(logo)
const openBtn = document.getElementById("open-btn");
const closeBtn = document.getElementById("close-btn");
const myNav = document.getElementById("my-nav");

openBtn.addEventListener('click', function(){
    myNav.style.display = 'block';
});

closeBtn.addEventListener('click', function(){
    myNav.style.display = 'none';
})
