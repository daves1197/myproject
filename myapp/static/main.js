

function rate(id) {
    const btn = document.querySelector('#btn');
    const actual_rating = document.querySelector('#rating');
    var sb = document.querySelector('#counter').innerHTML;
    let value1 = actual_rating.innerHTML;
    let value2 = 0;

    var radios = document.getElementsByName('rate');

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {

            value2 = radios[i].value;

            break;
        }
    }

    value1 = parseFloat(value1);
    var overall2 = parseInt(sb, 10);
    value2 = parseFloat(value2);

    var value3 = value2 + value1;
    console.log(sb);
    console.log(value1);
    console.log(value2);
    console.log(value3);
    let final = value3 / overall2;
    console.log(final);


        fetch(`/detailseminar/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                rating: final,
                counter: sb
            })
        });

        actual_rating.innerHTML = final;
        sb.innerHTML = sb;
   
}