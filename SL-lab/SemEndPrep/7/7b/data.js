window.onload = function(){
    Cars = [
        {
            'model':'Spark',
            'name':'chevrolet',
            'price':400000,
            'year':2006
        },
        {
            'model':'i20',
            'name':'Hyundai',
            'price':600000,
            'year':2009
        },
        {
            'model':'Cybertruck',
            'name':'Tesla',
            'price':5000000,
            'year':2019
        }
    ]

    for(var i=0;i<Cars.length;i++){
        elem = document.createElement("tr")
        elem.id=Cars[i]['model']
        elem.innerHTML = "<td>"+Cars[i]['model']+"</td>"
        document.getElementById('cars-menu').appendChild(elem)
    }

    Cars.forEach(mouseEventHandler)

    function mouseEventHandler(item){
        car = document.getElementById(item.model)

        car.onmouseover = function(){
            // document.getElementById('details').hidden = false
            document.getElementById('details').removeAttribute('hidden')
            document.getElementById('name').innerHTML = item.name
            document.getElementById("picture").innerHTML = "<img src='' alt='name of car'></img>"
            document.getElementById("price").innerHTML = item.price
            document.getElementById('year').innerHTML = item.year
        }
    }
}

