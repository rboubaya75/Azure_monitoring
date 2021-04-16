import axios from "axios";
import { useEffect, useState } from 'react';
import Chart from "react-google-charts";

function Charts(props) {
  const [costs, setCosts] = useState([]);
  
  const pieOptions = {
      title: props.name,
      sliceVisibilityThreshold: 0,
      pieHole: 0,
      slices: [
        {
          color: "#2BB673"
        },
        {
          color: "#d91e48"
        },
        {
          color: "#007fad"
        },
        {
          color: "#e9a227"
        }
      ],
      legend: {
        alignment: "center",
        textStyle: {
          color: "233238",
          fontSize: 14
        }
      },
      tooltip: {
        showColorCode: true
      },
      chartArea: {
        left: 500,
        top: 50,
        width: "50%",
        height: "80%"
      },
      fontName: "Roboto",
      fontSize: 20
  };

  useEffect(() => {
    const f = async() => {
          const res = await axios(`https://brtazuremonitor.azurewebsites.net/api/cost/${props.page}/${props.name}`)
          let tmp;
          if (props.page === 'subscriptions') {
            tmp = res.data.map(e => [e.service, e.cost])
          }
          else if (props.page === 'services') {
            tmp = res.data.map(e => [e.subscription, e.cost])
          }
          setCosts([['Name', 'Total'], ...tmp]);
    };
    f()
  }, [props.name, props.page]);
  return (
    <div className="charts">
      <Chart
        chartType="PieChart"
        data={costs}
        options={pieOptions}
        graph_id="PieChart"
        width={"100%"}
        height={"400px"}
        legend_toggle
      />
    </div>
  );
}

export default Charts;