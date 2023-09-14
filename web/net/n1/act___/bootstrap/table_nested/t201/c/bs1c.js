






    //Run On HTML Build
    $(document).ready(function () {

        // you would probably be using templates here
        detailsTableHtml = $("#detailsTable").html();

        //Insert a 'details' column to the table
        var nCloneTh = document.createElement('th');
        var nCloneTd = document.createElement('td');
        nCloneTd.innerHTML = '<img src="http://i.imgur.com/SD7Dz.png">';
        nCloneTd.className = "center";

        $('#exampleTable thead tr').each(function () {
            this.insertBefore(nCloneTh, this.childNodes[0]);
        });

        $('#exampleTable tbody tr').each(function () {
            this.insertBefore(nCloneTd.cloneNode(true), this.childNodes[0]);
        });


        //Initialse DataTables, with no sorting on the 'details' column
        var oTable = $('#exampleTable').dataTable({
            "bJQueryUI": true,
            "aaData": newRowData,
            "bPaginate": false,
            "aoColumns": [
                {
                   "mDataProp": null,
                   "sClass": "control center",
                   "sDefaultContent": '<img src="http://i.imgur.com/SD7Dz.png">'
                },
                { "mDataProp": "race" },
                { "mDataProp": "year" },
                { "mDataProp": "total" }
            ],
            "oLanguage": {
			    "sInfo": "_TOTAL_ entries"
			},
            "aaSorting": [[1, 'asc']]
        });

        /* Add event listener for opening and closing details
        * Note that the indicator for showing which row is open is not controlled by DataTables,
        * rather it is done here
        */
        $('#exampleTable tbody td img').live('click', function () {
            var nTr = $(this).parents('tr')[0];
            var nTds = this;

            if (oTable.fnIsOpen(nTr)) {
                /* This row is already open - close it */
                this.src = "http://i.imgur.com/SD7Dz.png";
                oTable.fnClose(nTr);
            }
            else {
                /* Open this row */
                var rowIndex = oTable.fnGetPosition( $(nTds).closest('tr')[0] );
	            var detailsRowData = newRowData[rowIndex].details;

                this.src = "http://i.imgur.com/d4ICC.png";
                oTable.fnOpen(nTr, fnFormatDetails(iTableCounter, detailsTableHtml), 'details');
                oInnerTable = $("#exampleTable_" + iTableCounter).dataTable({
                    "bJQueryUI": true,
                    "bFilter": false,
                    "aaData": detailsRowData,
                    "bSort" : true, // disables sorting
                    "aoColumns": [
                    { "mDataProp": "pic" },
	                { "mDataProp": "name" },
	                { "mDataProp": "team" },
	                { "mDataProp": "server" }
	            ],
                    "bPaginate": false,
                    "oLanguage": {
						"sInfo": "_TOTAL_ entries"
			        },
                    "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
                      var imgLink = aData['pic'];
                      var imgTag = '<img width="100px" src="' + imgLink + '"/>';
                      $('td:eq(0)', nRow).html(imgTag);
                     return nRow;
                    }
                });
                iTableCounter = iTableCounter + 1;
            }
        });

    });
  </script>


