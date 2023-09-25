
//    '<thead><tr><th>References</th><th>Section</th><th>Statute Titles</th><th>Info</th></tr></thead>'+
function format1 ( arg_table_id ) {
    return '<table class="table table-striped" id="'+tbl1_name+'_'+arg_table_id+'"></table>';
}




$(document).ready(function() {
	// TableHtml = $('#opiniondt').html();

    //var table = $('#opiniondt').DataTable( {

    //var table = $('#myTable1').DataTable( {
    var myTableVar1 = $(tbl1_id).DataTable( {
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

    $(tbl1_id+" tbody tr").each(function(index) {
    	$(this).attr('index', index);
    })

    /* Add event listener for opening and closing details
     * Note that the indicator for showing which row is open is not controlled by DataTables,
     * rather it is done here
     */
     $(tbl1_id+' tbody').on('click', 'td.details-control', function () {
         var tr = $(this).closest('tr');
         var row = myTableVar1.row( tr );

         if ( row.child.isShown() ) { //  This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
         } else { // Open this row
            row.child( format1(TableCounter) ).show();
            //alert( 'Row index: '+row.index() );

            tr.addClass('shown');
            // try datatable stuff
            TableInner = $(tbl1_id+'_' + TableCounter).dataTable({
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
                   {
                      "targets": -1,
                       "data": null,
                      "defaultContent": "<button href='"+row.index()+"' class='button-info'>Click Me!</button>"
                   }
                 ]
            });
            TableCounter = TableCounter + 1;
            var index = $(this).closest('tr').index();
            var data = sections[index];
        }
     });


  	$('table').on( 'click', 'td .button-info', function () {
        var parent = $(this).closest('table').parents('tr').index();
        var parentIndex = $('tbody tr:nth-child('+(parent)+')').attr('index');
        var currentIndex = $(this).closest('tr').index();
        var data = sections[parentIndex][currentIndex];
        console.log(data);
        return;
        //window.open("/info.php?name=" + data.name + "&sal=" + data.salary);
    } );

} );
