function HourMinute(num)
{
    if(num<60)
        return "0:"+num
    else
        return Math.floor(num/60)+":"+(num%60)
}
console.log(HourMinute(126))