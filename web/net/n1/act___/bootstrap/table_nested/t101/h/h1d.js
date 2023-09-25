/**
 *
 */
var tbl2_name='myTable2'
var tbl2_id='#'+tbl2_name


/**
 *
 */
function format2 ( arg_table_id ) {
    return '<table class="table table-striped" id="'+tbl2_name+'_'+arg_table_id+'">'+
    '</table>';
}


$(document).ready(function() {

    var myNestedTable2var = $(tbl2_id).DataTable( {
      paging: false,
      searching: false,
      info: false,
      rowId: 'id',
      data: opinions,
      columns:[
        { className:      'details-control',
          orderable:      false,
          data:           null,
          defaultContent: '' },
        { data:'date'},
        { data:'name'}
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
                data: sections[row.index()],
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
                   { data:'position' },
                   { data:'salary' },
                 ]
            });
            TableCounter = TableCounter + 1;
            var index = $(this).closest('tr').index();
            var data = sections[index];
        }
     });


});


