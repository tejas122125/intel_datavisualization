import React from "react";
import Plot from "react-plotly.js";
import { Data } from "@/lib/data";

interface BarChartProps {
  data: Data[];
  onClick: (category: string) => void;
}

const Barchart: React.FC<BarChartProps> = ({ data, onClick }) => {
  const categories = data.map((d) => d.Category);
  const values = data.map((d) => d.Values);

  const handleClick = (event: any) => {
    if (event.points.length > 0) {const category = event.points[0].x;
    onClick(category);
    }
  };
  return(
    <Plot
     data = {[
        {
            x:categories,
            y:values,
            type:'bar',
        }
     ]}
     layout ={{title:'Category vs Values'}}
     onClick = {handleClick}
     />
  );
};

export default Barchart;
