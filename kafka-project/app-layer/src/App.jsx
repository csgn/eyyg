import axios from "axios";
import { useState, useEffect } from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const data = [
  {
    name: "01/01/2020",
    200: 15,
    404: 3,
    303: 8,
    500: 20,
  },
  {
    name: "02/01/2020",
    200: 10,
    404: 4,
    303: 2,
    500: 2,
  },
  {
    name: "03/01/2020",
    200: 7,
    404: 3,
    303: 2,
    500: 8,
  },
  {
    name: "04/01/2020",
    200: 5,
    404: 3,
    303: 8,
    500: 0,
  },
  {
    name: "05/01/2020",
    200: 4,
    404: 2,
    303: 9,
    500: 1,
  },
  {
    name: "06/01/2020",
    200: 1,
    404: 9,
    303: 2,
    500: 3,
  },
  {
    name: "07/01/2020",
    200: 2,
    404: 8,
    303: 2,
    500: 5,
  },
];

const tabs = [
  {
    id: 0,
    text: "/usr",
  },
  {
    id: 1,
    text: "/usr/login",
  },
  {
    id: 2,
    text: "/usr/admin",
  },
  {
    id: 3,
    text: "/usr/register",
  },
];

function StatusChart({ title, data, lines }) {
  return (
    <div className="mt-20 flex items-center">
      <span className="text-2xl text-indigo-500">{title}</span>
      <ResponsiveContainer width="100%" height={325}>
        <LineChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          {/*           <CartesianGrid strokeDasharray="3 3" /> */}
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          {lines.map((line) => (
            <Line
              type="monotone"
              dataKey={line.key}
              stroke={line.stroke}
              activeDot={{ r: 8 }}
            />
          ))}
          // lines
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

function Tabs({ tabs, step = 0, onChange }) {
  const [selected, setSelected] = useState(0);

  const handleSelect = (index) => {
    setSelected(index);
  };

  useEffect(() => {
    if (onChange) onChange(selected);
  }, [selected]);

  useEffect(() => {
    setSelected(step);
  }, [step]);

  return (
    <div className="flex flex-row justify-start border-solid border-b-gray-600 overflow-x-scroll w-full rounded-bl-lg bg-[#11111100] rounded-bl-lg rounded-br-lg sticky">
      {tabs.map((tab, index) => (
        <div
          className={`inline-block hover:opacity-60 ${
            index === selected
              ? "bg-[#621cbd44] border-[#621cbd] border-b-4 text-[#eee]"
              : "bg-inherit border-b-[#333] border-b-4 text-[#999]"
          } cursor-pointer  p-4 flex w-full transition ease-in-out delay-40 duration-300 `}
          active={index === selected}
          key={index}
          onClick={() => handleSelect(index)}
        >
          {tab.text}
        </div>
      ))}
    </div>
  );
}

function App() {
  const [step, setSteo] = useState(0);
  const [endpoints, setEndpoints] = useState([]);

  const getEndpoints = () => {
    axios
      .get(`${process.env.BACKEND_API_URL}/api/endpoints`)
      .then((res) => {
        setEndpoints(res.data);
      })
      .catch((err) => {});
  };

  return (
    <>
      <div className="container md:mx-auto pb-20 h-auto relative">
        <Tabs
          tabs={tabs}
          step={step}
          onChange={(e) => {
            setSteo(e);
          }}
        />

        <StatusChart
          title="GET"
          data={data}
          lines={[
            {
              key: "200",
              stroke: "#fff",
            },
            {
              key: "303",
              stroke: "#fff",
            },
            {
              key: "404",
              stroke: "#fff",
            },
            {
              key: "500",
              stroke: "#fff",
            },
          ]}
        />

        <StatusChart
          title="GET"
          data={data}
          lines={[
            {
              key: "200",
              stroke: "#fff",
            },
            {
              key: "303",
              stroke: "#fff",
            },
            {
              key: "404",
              stroke: "#fff",
            },
            {
              key: "500",
              stroke: "#fff",
            },
          ]}
        />
        <StatusChart
          title="GET"
          data={data}
          lines={[
            {
              key: "200",
              stroke: "#fff",
            },
            {
              key: "303",
              stroke: "#fff",
            },
            {
              key: "404",
              stroke: "#fff",
            },
            {
              key: "500",
              stroke: "#fff",
            },
          ]}
        />
        <StatusChart
          title="GET"
          data={data}
          lines={[
            {
              key: "200",
              stroke: "#fff",
            },
            {
              key: "303",
              stroke: "#fff",
            },
            {
              key: "404",
              stroke: "#fff",
            },
            {
              key: "500",
              stroke: "#fff",
            },
          ]}
        />
      </div>
    </>
  );
}

export default App;
