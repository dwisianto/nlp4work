// https://jsfiddle.net/udgp3x9o/26/
function hw() {
    console.log('hello world');
}



var sections = [
    [{
        "eventtime": "2016-10-07 13:55:21",
        "device": "01",
        "ip": "10.10.232.3",
        "info": "ad0\/8\/0\/0",
        "remark": "116"
    }, {
        "eventtime": "2016-10-07 13:55:21",
        "device": "10-01",
        "ip": "10.10.242.3",
        "info": "N/A",
        "remark": "N/A"
    }, {
        "eventtime": "2016-10-07 13:55:21",
        "device": "10-01",
        "ip": "10.10.240.3",
        "info": "N/A",
        "remark": "N/A"
    }, {
        "eventtime": "2016-10-07 13:55:21",
        "device": "10-01",
        "ip": "10.10.243.3",
        "info": "ad0\/6\/1\/4",
        "remark": "64"
    }],
    [{
        "eventtime": "2016-10-03 10:52:11",
        "device": "01",
        "ip": "10.10.230.3",
        "info": "ad0\/8\/0\/2",
        "remark": "74"
    }, {
        "eventtime": "2016-10-03 10:52:15",
        "device": "AHL",
        "ip": "10.110.201.42",
        "info": "N\/A",
        "remark": "N\/A"
    }],
    [{
        "eventtime": "2016-10-03 10:52:11",
        "device": "10-01",
        "ip": "10.10.246.3",
        "info": "ad0\/6\/1\/2",
        "remark": "62"
    }, {
        "eventtime": "2016-10-03 10:52:11",
        "device": "10-01",
        "ip": "10.10.10.3",
        "info": "ad0\/6\/1\/0",
        "remark": "32"
    }, {
        "eventtime": "2016-10-03 10:52:11",
        "device": "01",
        "ip": "10.10.230.3",
        "info": "ad0\/7\/0\/8",
        "remark": "120"
    }, {
        "eventtime": "2016-10-03 10:52:11",
        "device": "01",
        "ip": "10.10.246.3",
        "info": "ad0\/7\/1\/1",
        "remark": "25"
    }, {
        "eventtime": "2016-10-03 10:52:11",
        "device": "01",
        "ip": "10.10.12.3",
        "info": "ad0\/6\/1\/1",
        "remark": "33"
    }, {
        "eventtime": "2016-10-03 10:52:11",
        "device": "01",
        "ip": "10.10.230.3",
        "info": "ad0\/8\/0\/2",
        "remark": "74"
    }, {
        "eventtime": "2016-10-03 10:52:15",
        "device": "AHL",
        "ip": "10.110.201.42",
        "info": "N\/A",
        "remark": "N\/A"
    }]
];



function format(table_id) {
    return '<table class="table table-striped" id="opiniondt_' + table_id + '">' +
        '<thead><tr><th>timestamp</th><th>user</th><th>loc</th><th>info</th><th>remark</th><th>more</th></tr></thead>' +
        '<tr>' +
        '<td>Timestamp:</td>' +
        '<td>Device:</td>' +
        '<td>info:</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Timestamp:</td>' +
        '<td>Device:</td>' +
        '<td>info:</td>' +
        '</tr>' +
        '</table>';
}
var iTableCounter = 1;
var oInnerTable;

// $(document).ready(function() {
function hw2(){
    TableHtml = $('#opiniondt').html();

        var table = $('#opiniondt').DataTable({
            paging: false,
            searching: false,
            info: true,
            searching: true,
            rowId: 'aggr_id',
            jQueryUI: true,
            data: options,
            columns: [{
                className: 'details-control',
                orderable: false,
                data: null,
                defaultContent: ''
            }, {
                data: 'starttime'
            }, {
                data: 'rs'
            }, {
                data: 'loc'
            }, {
                className: 'index hidden',
                data: 'index'
            }],
            order: [
                [1, 'asc']
            ]
        });
        /* Add event listener for opening and closing details
         * Note that the indicator for showing which row is open is not controlled by DataTables,
         * rather it is done here
         */
        $("table tbody tr").each(function(index) {
            $(this).attr('index', index);
        })
        $('#opiniondt tbody').on('click', 'td.details-control', function() {
            var tr = $(this).closest('tr');
            var row = table.row(tr);

            if (row.child.isShown()) {
                //  This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            } else {
                // Open this row
                row.child(format(iTableCounter)).show();
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
                    columns: [{
                        data: 'eventtime'
                    }, {
                        data: 'device'
                    }, {
                        data: 'ip'
                    }, {
                        data: 'info'
                    }, {
                        data: 'remark'
                    }, {
                        data: null,
                        "render": function ( data, type, full, meta ) {
                                     if (full.info != 'N/A') {
                          return "<button href='" + row.index() + "' class='btn btn-info'>View</button>"
        } else {
            return ""
        }
        }
                       // "defaultContent": "<button href='" + row.index() + "' class='btn btn-info'>Hello</button>"
                            //"defaultContent": "<button class='btn btn-info'>View</button>"
                    }]
                });
                iTableCounter = iTableCounter + 1;
                var index = $(this).closest('tr').index();
                var data = sections[index];
            }
        });

        $('table').on('click', 'td .btn-info', function() {
            var parent = $(this).closest('table').parents('tr').prev();
            var parentIndex = parent.find('.index').text();
            var currentIndex = $(this).closest('tr').index();
            var data = sections[parentIndex][currentIndex];

        });

    });

}
