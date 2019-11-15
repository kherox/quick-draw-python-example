
const canvas = document.querySelector("canvas");

canvas.width = 240;
canvas.height = 240;


const context = canvas.getContext("2d");

context.strokeStyle = "#ff4141";
context.lineWidth = 10;
context.lineCap = "round";

let shouldPaint = false

canvas.addEventListener("mouseup",(e)=>{
    shouldPaint = false;
   
})

canvas.addEventListener("mousedown",(e)=>{
    shouldPaint = true ; 
    context.moveTo(e.pageX , e.pageY);
    context.beginPath()
})

canvas.addEventListener("mousemove",(event) => {

    if (shouldPaint){
        context.lineTo(event.pageX , event.pageY);
        context.stroke()
    }

})


canvas.addEventListener("mouseleave",function(e){
    if (shouldPaint){
    var img = document.createElement("img");
       img.src = canvas.toDataURL("image/png");
       document.body.append(img);

       // document.querySelector("img"). = context.getImageData(140,140,140,140).data
        console.log(context.getImageData(240,240,240,40))
    }
    
})


document.querySelectorAll("nav a").forEach(link => {

    link.addEventListener("click",function(e){
        context.strokeStyle = this.style.backgroundColor
    })



})