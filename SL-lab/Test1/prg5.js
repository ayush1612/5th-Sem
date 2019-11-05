function OddRange(num1,num2)
{
    odd = []
    for(var i = num1+1;i<num2;i++)
        if(i%2 != 0)
            odd.push(i)
    return odd
}

console.log(OddRange(1,25))