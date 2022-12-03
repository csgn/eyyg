import axios from "axios";
import { useState, useEffect } from "react";

import strokes from "./static/strokes";


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


function Spinner() {
  return (
    <div role="status">
      <svg
        aria-hidden="true"
        className="mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-indigo-600"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
    </div>
  );
}

function StatusChart({ url, method, title }) {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  let lines = [];

  const getData = async () => {
    setLoading(true);

    await axios
      .get(`${import.meta.env.VITE_BACKEND_API_URL}/api/whole-time?url=${url}&method=${method}`)
      .then((res) => {
        setTimeout(() => {
          const t = [];
          const d = res.data.map((el) => {
            el.request_time = el.request_time.split("T")[0];
            return {
              time: el.request_time,
              count: el.count,
              status: el.request_status,
            };
          });
          const ll = [];

          d.map((el) => {
            const l = ll.filter((l) => l.time === el.time);

            if (l.length === 0) {
              ll.push({
                time: el.time,
                [el.status]: el.count,
              });
            } else {
              l[0][el.status] = el.count;
            }
          });

          setData(ll);

          setLoading(false);
        }, 500);
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getData();
  }, [url]);

  if (data.length > 0) {
    lines = Object.keys(data[0] ?? []).filter((e) => e !== "time");
  }

  console.log(lines);

  return (
    <div className="flex items-center">
      <div className="w-48">
        <span className="text-2xl text-indigo-500">{title}</span>
      </div>
      {loading ? (
        <Spinner />
      ) : (
        <ResponsiveContainer width="100%" height={325}>
          <>
            <LineChart
              width={1024}
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
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Legend />
              {lines.map((line) => (
                <Line
                  type="monotone"
                  dataKey={line}
                  stroke={strokes[line]}
                  activeDot={{ r: 8 }}
                />
              ))}
            </LineChart>
          </>
        </ResponsiveContainer>
      )}
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
          {tab}
        </div>
      ))}
    </div>
  );
}

function Content({ url }) {
  const [methods, setMethods] = useState([]);

  const getMethods = async () => {
    await axios
      .get(`${import.meta.env.VITE_BACKEND_API_URL}/api/methods?url=${url}`)
      .then((res) => {
        setMethods(res.data);
      })
      .catch((err) => {});
  };

  useEffect(() => {
    getMethods();
  }, []);

  return (
    <div className="flex flex-col w-full relative mt-20 gap-8">
      {methods.map((method) => (
        <StatusChart url={url} method={method} title={method} />
      ))}
    </div>
  );
}

function App() {
  const [step, setStep] = useState(0);
  const [endpoints, setEndpoints] = useState([]);

  const [loading, setLoading] = useState(true);

  const getEndpoints = async () => {
    await axios
      .get(`${import.meta.env.VITE_BACKEND_API_URL}/api/endpoints`)
      .then((res) => {
        setEndpoints(res.data);
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getEndpoints();
  }, []);

  if (loading) return <p>loading ...</p>;

  return (
    <>
      <div className="container md:mx-auto pb-20 h-auto relative w-full">
        <Tabs tabs={endpoints} step={step} onChange={setStep} />
        <Content url={endpoints[step]} />
      </div>
    </>
  );
}

export default App;
