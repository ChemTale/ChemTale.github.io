// This is the string you receive (with an extra "" that you mentioned)

function parse_str(stringList){

    // Remove the outermost quotes
    //stringList = stringList.substring(1, stringList.length - 1);
    
    // Replace single quotes with double quotes to make it JSON compatible
    stringList = stringList.replace(/'/g, '\"');
    
    // Parse the string into a JavaScript array
    const videoList = JSON.parse(stringList);
    
    return videoList
}

console.log(parse_str("['/watch?v=VmTZcNVzp7A&pp=ygURaG93IHRvIGNyZWF0ZSBIMk8%3D', '/VdNPkW9I0fQ', '/watch?v=s67yDuPfI8E&pp=ygUTaG93IHRvIGNyZWF0ZSBIMlNPNA%3D%3D']"))