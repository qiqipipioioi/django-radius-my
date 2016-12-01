  $(function(){
    var myElement= document.getElementById('carousel-show')
    var hm=new Hammer(myElement);
    hm.on("swipeleft",function(){
        $('#carousel-show').carousel('next')
    })
    hm.on("swiperight",function(){
        $('#carousel-show').carousel('prev')
    })
})
