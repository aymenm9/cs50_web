// get the btns left and right & the img + btn div all set to d-none
const btns = document.getElementsByClassName("listing-img-btn")
const imgs = document.getElementsByClassName("listing-img")


var imgs_n = imgs.length
var currentImgIndex = 0 
// dsplay the first img div
imgs[0].classList.remove("d-none")
console.log(btns)
console.log(imgs)


// got to the next img left or rigth if it is out of the array go back in loop 
for( let i = 0 ; i< btns.length; i++ ){
    console.log("i hate js")
    console.log(btns[i])
    btns[i].addEventListener("click", function(){
        
        if (btns[i].classList.contains("right")){
            imgs[currentImgIndex].classList.add("d-none")
            currentImgIndex = (currentImgIndex + 1) % imgs_n
            imgs[currentImgIndex].classList.remove("d-none")
            console.log(currentImgIndex)
        }
        else{
            imgs[currentImgIndex].classList.add("d-none")
            // js have broking mod operator add n imgs_n dosn't tchange the reslt this added to not get negativ nuber
            currentImgIndex = (currentImgIndex - 1 + imgs_n ) % imgs_n
            console.log(currentImgIndex)
            imgs[currentImgIndex].classList.remove("d-none")
            console.log(currentImgIndex)
        }
    })
}