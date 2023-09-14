// https://jsfiddle.net/dushdushyant/zrh17b5g/83/
// https://jsfiddle.net/udgp3x9o/13/
function hw(){
    console.log('hello world');
}


var opinions = [
    {"id":47, "name":"E061140","title":"Eustice","opinionDate":"2015-12-10"},
    {"id":48, "name":"C070296M","title":"Nilsson","opinionDate":"2015-12-10"},
    {"id":50, "name":"S209643","title":"Stevens","opinionDate":"2015-12-10"}
    ];


var sections = [
    [
        {"name": "Tiger Nixon",     "position": "System Architect", "salary": "$3,120" },
        {"name": "Garrett Winters", "position": "Director",         "salary": "$5,300"}
    ],
    [
        {"name": "Sarah Haslimier",  "position":   "Project Manager", "salary": "$7,220" },
        {"name": "Liam Neilson",     "position":   "Cup Holder",      "salary": "$1,010" },
        {"name": "Tomas Tomlingtom", "position":   "Busybody",        "salary": "$9,910" },
    ],
    []
];

console.log(sections[0]);
console.log(sections);


function format ( table_id ) {
    return '<table class="table table-striped" id="opiniondt_'+table_id+'">'+
    '<thead><tr><th>References</th><th>Section</th><th>Statute Titles</th><th>Info</th></tr></thead>'+
    '<tr>'+
      '<td>Full name:</td>'+
      '<td>Extension number:</td>'+
      '<td>Extra info:</td>'+
    '</tr>'+
    '<tr>'+
      '<td>Full name:</td>'+
      '<td>Extension number:</td>'+
      '<td>Extra info:</td>'+
    '</tr>'+
    '</table>';
}
var iTableCounter=1;
var oInnerTable;


$(document).ready(function() {
	TableHtml = $('#opiniondt').html();

    var table = $('#opiniondt').DataTable( {
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
        { data:'opinionDate'},
        { data:'title'},
        { data:'name'}
      ],
      order: [[1, 'asc']]
    } );

    $("table tbody tr").each(function(index) {
    	$(this).attr('index', index);
    })

    /* Add event listener for opening and closing details
     * Note that the indicator for showing which row is open is not controlled by DataTables,
     * rather it is done here
     */
     $('#opiniondt tbody').on('click', 'td.details-control', function () {
         var tr = $(this).closest('tr');
         var row = table.row( tr );

         if ( row.child.isShown() ) { //  This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
         } else { // Open this row
            row.child( format(iTableCounter) ).show();
            //alert( 'Row index: '+row.index() );

            tr.addClass('shown');
            // try datatable stuff
            oInnerTable = $('#opiniondt_' + iTableCounter).dataTable({
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
                   { data:'name' },
                   { data:'position' },
                   { data:'salary' },
                   {
                      "targets": -1,
                       "data": null,
                      "defaultContent": "<button href='"+row.index()+"' class='button-info'>Click Me!</button>"
                   }
                 ]
            });
            iTableCounter = iTableCounter + 1;
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
