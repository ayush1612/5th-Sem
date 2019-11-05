function LetterSurround(str)
{
    if((str.charAt(0)>='a'&&str.charAt(0)<='z') || (str.charAt(str.length-1) >= 'a' && str.charAt(str.length - 1) <= 'z'))
    {
        return false;
    }

    for(var i=1;i<str.length-1;i++)
    {
        if(str.charAt(i)>='a' && str.charAt(i)<='z')
        {
            if(str.charAt(i-1)!='+' || str.charAt(i+1) != '+')
                return false;
        }
    }
    return true;
}

console.log(LetterSurround("f++d+"))