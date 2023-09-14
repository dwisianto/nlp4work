


function hw() {
    console.log('hello world');


    var options = [{
        "age":20,
        'date':"2016-10-03,
        'name':'def',
        "aggr_id": "5",
        "starttime": "2016-10-03 10:52:15",
        "rs": "user error ",
        "loc": "ad0/7/0/19,"
    }, {
        "age":40,
        'date':"2016-10-03,
        'name':'abc'
        "aggr_id": "5",
        "starttime": "2016-10-03 10:52:15",
        "rs": "pwd error ",
        "loc": "2-02_ad0/7/0/19"
    }];

    for (var x in options) {
        options[x].index = x;
    }
    console.log(options);

	TableHtml = $('#opiniondt').html();
    var table = $('#opiniondt').DataTable({
        paging: false,
        searching: false,
        info: true,
        rowId: 'age',
        data: options,
        columns:[
        { className:      'details-control',
          orderable:      false,
          data:           null,
          defaultContent: '' },
        { data:'date'},
        { data:'title'},
        { data:'name'}
      ],
      order: [[1, 'asc']]
    });




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

}

