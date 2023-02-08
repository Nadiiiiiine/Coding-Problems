exemple de rep 

javascript :

print(Math.round(d%2==0?(9/5*d)+32:(d-32)*(5/9)))


const d = parseInt(readline());
if (d % 2 === 1) {
    console.log(Math.round((d-32)*(5/9)));
} else {
    console.log(Math.round((9/5 * d) + 32));
}
