


function hw(){
    console.log('hello world');

    var innerTblData='{"data" : [ ["__", "aaa", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] , ["__", "bbb", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] ] }';

    var innerTblData2='{"data" : [ ["__", "zzza", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] , ["__", "bbb", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] ] }';
    var table = $('#example').DataTable({buttons:[{extend:'copy',exportOptions:{columns:':visible'}},'colvis'],dom:'lbfrtip'});

    // Add event listener for opening and closing details
    $('#example').on('click', 'td.details-control', function (e) {
    //e.stopPropagation();
    console.log("click parent");
        var tr = $(this).closest('tr');
       var indexx= $(this).parent().index();
        console.log('eda'+indexx);
        var row = table.row(tr);
        console.log('row '+row.value);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        } else {
            // Open this row
            if(indexx==0){
             loadInnerTbl(row);
            }else{
            loadInnerTbl2(row);
            }

             tr.addClass('shown');
        }
    });

    function loadInnerTbl(row) {

    var table = $('#chileTbl1').clone().dataTable( {
            "sDom": 'ti',
            "deferRender": true,
            "processing": true,
            "ajax": '/echo/js/?js='+innerTblData
        });

        table.removeClass("childtable_hidden");
        var child = row.child(table);
       var table_td =$(table).closest('tr td');
       table_td.addClass("nestedtable");
       child.show();
    }
     function loadInnerTbl2(row) {

    var table = $('#chileTbl1').clone().dataTable( {
            "sDom": 'ti',
            "deferRender": true,
            "processing": true,
            "ajax": '/echo/js/?js='+innerTblData2
        });

        table.removeClass("childtable_hidden");
        var child = row.child(table);
       var table_td =$(table).closest('tr td');
       table_td.addClass("nestedtable");
       child.show();
    }



    var arrOfTable1=[],
 i=0;

$('#example td').each(function() {
 mWid = $(this).width();
 arrOfTable1.push(mWid);
});

//console.log(arrOfTable1);

$('#loadBtn').on( "click", function() {
    innerTblData='{"data" : [ ["__", "sdfsf", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] , ["__", "bbb", "2", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"] ] }';
    var myJson = $.parseJSON(innerTblData);
    myJson['data'].push("__,jhgasdjaf,dadda,1,2,1,1,1,2,1,1");
    $.each(myJson, function(index,jsonObject){
    console.log("Key "+index);
    $.each(jsonObject, function(key,val){
        console.log("index "+val);
    });
});
innerTblData=JSON.stringify(myJson);
 console.log("formatted "+innerTblData);
});


}

