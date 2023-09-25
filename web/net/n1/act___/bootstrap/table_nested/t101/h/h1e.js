var dataArray = [
   {
      "id":28,
      "Title":"Sweden",
      "tag": [["In","IN"],["Stanley","NNP"],]
   },
   {
      "id":56,
      "Title":"USA",
      "tag": [["In","IN"],["Stanley","NNP"],]
   },
   {
      "id":89,
      "Title":"England",
      "tag": [["In","IN"],["Stanley","NNP"],]
   }
];

//var aoa = [ ['a','b'], ['c','d'] ];


$(document).ready(function() {

    console.log("hi");
    // console.log( JSON.stringify(tag) );
    var outArr = $(jQuery.parseJSON(JSON.stringify(dataArray))).map(function(){
        return {'tag':this.tag};
    });
    console.log(outArr);
});

/*
    $(jQuery.parseJSON(JSON.stringify(dataArray))).each(function() {
        var ID = this.id;
        var TITLE = this.Title;
        console.log(ID)
        console.log(TITLE)
    });

    var outArr = $(jQuery.parseJSON(JSON.stringify(dataArray))).map(function() {
        return [{'ID':this.id}, {'TITLE':this.Title}];
    });
    console.log(outArr);
*/

