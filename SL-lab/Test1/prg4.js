function AgeConvert(num)
{
    var ageParams = num.split('-');
    var day = Number(ageParams[0])
    var month = Number(ageParams[1])
    var year = Number(ageParams[2])

    var d = new Date();
    
    var currentDate = d.getDate();
    var currentMonth = d.getMonth() + 1;
    var currentYear = d.getFullYear();
    
    var age = currentYear - year

    if(currentMonth < month)
        age--;
    else if(currentMonth == month)
    {
        if(currentDate < date)
            age--;
    }
    return age;
}

console.log(AgeConvert('28-02-1992'))