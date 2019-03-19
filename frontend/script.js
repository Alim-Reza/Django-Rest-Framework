            $(function(){
            // $("button").click(function () {
            //     console.log("1");
            //     var data = {

            //     }
            //     $.post("http://127.0.0.1:8000/api/employees/",
            //         {
            //             csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            //             fname: $("#form input[name=firstname]").val(),
            //             lname: $("#form input[name=lastname]").val(),
            //             rage: $("#form input[name=age]").val()
            //         },
            //         function (response) {
            //             console.log("2");
            //             if (response.success == false) {
            //                 alert("there are some problem!");
            //             }
            //             else {
            //                 window.location.href = "employee.html"
            //             }
            //         });
            // });

            $.get( "http://127.0.0.1:8000/api/employees/", function( data ) {
                $( ".result" ).html( data );
                console.log("ay hai chicken dinner");
            });

        });