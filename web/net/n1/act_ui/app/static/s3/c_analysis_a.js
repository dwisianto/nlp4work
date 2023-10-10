// https://stackoverflow.com/questions/1140402/how-to-add-jquery-in-js-file
/**
 *
 */
var tbl2_name='myTable2'
var tbl2_id='#'+tbl2_name
var TableCounter=1; // replacing var iTableCounter
var TableInner // replacing var oInnerTable;


/**
 *
 */
function format2 ( arg_table_id ) {
    return '<table class="table table-striped" id="'+tbl2_name+'_'+arg_table_id+'">'+
    '</table>';
}

/*
  //console.log(typeof(outArr));
    //console.log(Object.keys(outArr).length);
    //console.log(outArr.length);
    //console.log(outArr);
    //console.log(outArr[0]);
    //console.log( Object.keys(outArr[0]["snt"]).length);
*/
function getObjSnt(objVar){

    var objArr = $(jQuery.parseJSON(JSON.stringify(objVar))).map(function(){
            return {'snt':this.snt, 'snt_id': this.snt_id };
        });

    //console.log(objArr)
    delete objArr.length;
    delete objArr.prevObject;
    //console.log(Object.values(objArr));

    return Object.values(objArr);
}

/*
    //console.log(typeof(outArr));
    //console.log(Object.keys(outArr).length);
    //console.log(outArr.length);
    //console.log(outArr);
    //console.log(outArr[0]);
    //console.log( Object.keys(outArr[0]["tag"]).length);
*/
function getObjTag(objVar){

    var objArr = $(jQuery.parseJSON(JSON.stringify(objVar))).map(function(){
            return {'tag':this.tag};
        });

    console.log(objArr)
    delete objArr.length;
    delete objArr.prevObject;

    lst_of_tags = Object.keys(objArr).map((key) => objArr[key]["tag"] );
    // lst_of_entries = Object.keys(lst_of_tags).map((key) => Object.fromEntries(lst_of_tags[key]) );

    var lst_of_entries_loop = []
    for (let i = 0; i < lst_of_tags.length; i++) {
        lst_of_tags_loop = lst_of_tags[i]
        lst_of_entries = lst_of_tags_loop.map( (x) => ({'tkn':x[0],'tag':x[1]}) );
        //lst_of_entries = Object.keys(lst_of_tags_loop).map( (x) => {'tkn':x[0],'tag':x[1]}  );
        lst_of_entries_loop.push(lst_of_entries);
    }

    // return Object.keys(objArr).map((key) => objArr[key]["tag"] );
    return lst_of_entries_loop;
}


/**
 *
 */
function jquery_ajax_call_for_table_generation(inDataArray) {

    //console.log( inDataArray );
    var objTag = getObjTag(inDataArray);
    var objSnt = getObjSnt(inDataArray);
    console.log(objTag);
    // console.log(objSnt);


    var myNestedTable2var = $(tbl2_id).DataTable( {
      paging: false,
      searching: false,
      info: false,
      rowId: 'id',
      data: objSnt,
      columns:[
        { className:      'details-control',
          orderable:      false,
          data:           null,
          defaultContent: '' },
        { data:'snt_id'},
        { data:'snt'}
      ],
      order: [[1, 'asc']]
    } );


    /* Add event listener for opening and closing details
     * Note that the indicator for showing which row is open is not controlled by DataTables,
     * rather it is done here
     */
     $(tbl2_id+' tbody').on('click', 'td.details-control', function () {
         var tr = $(this).closest('tr');
         var row = myNestedTable2var.row( tr );

         if ( row.child.isShown() ) { //  This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
         } else { // Open this row
            row.child( format2(TableCounter) ).show();
            //alert( 'Row index: '+row.index() );

            tr.addClass('shown');
            // try datatable stuff
            TableInner = $(tbl2_id+'_' + TableCounter).dataTable({
                data: objTag[row.index()],
                autoWidth: true,
                deferRender: true,
                info: false,
                lengthChange: false,
                ordering: false,
                paging: false,
                scrollX: false,
                scrollY: false,
                searching: false,
               columns:[
                   { data:'tkn' },
                   { data:'tag' },
                 ]
            });
            TableCounter = TableCounter + 1;
            // var index = $(this).closest('tr').index();
            // var data = objTag[index];
        }
     });


}


/**
 *
 */
function jquery_ajax_call() {

  $.ajax({
    url:"/analysis/info",
    success:function(arrayOfObjects) {
      // console.log(arrayOfObjects);
      var outArr3 = jquery_ajax_call_for_table_generation(arrayOfObjects);
    },
    error:function(req, status, err){
        console.log('something went wrong', status, err);
    }
  });

}



$(document).ready(function () {
    jquery_ajax_call();
});
