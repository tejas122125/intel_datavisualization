import React from 'react'
import Plot from 'react-plotly.js'
import { Data } from '@/lib/data'

interface PieChartProps{
    data: Data[]
    onClick: (category: string) => void
}

const Piechart:React.FC<PieChartProps> = ({data}) => {
    const categories = data.map(d=>d.Category);
    const values = data.map(d=>d.Values);

    const handleClick = (event: any) => {
        if (event.points.length > 0) {const category = event.points[0].x;
        onClick(category);
        }
      };

  return (
    <Plot
        data={[
            {
            labels: categories,
            values: values,
            type: 'pie',
            },
        ]}
        layout={{ title: 'Category vs Values' }}
        onClick={handleClick}
  )
}

export default Piechart