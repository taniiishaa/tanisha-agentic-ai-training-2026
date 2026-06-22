function AboutMe() {
  const skills = [
    "Python",
    "C",
    "C++",
    "MySQL",
    "AWS",
    "Git",
    "GitHub",
    "HTML",
    "CSS",
    "Excel",
  ];

  return (
    <div className="min-h-screen bg-gray-100 p-8">

      {/* Navbar */}
      <div className="bg-slate-900 text-white rounded-lg px-8 py-5 flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Tanisha</h1>

        <button className="bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-lg">
          Download Resume
        </button>
      </div>

      <div className="max-w-6xl mx-auto flex flex-col md:flex-row gap-8">

        {/* Left Profile Card */}
        <div className="bg-slate-900 text-white p-8 rounded-3xl w-full md:w-1/3">

          <div className="w-24 h-24 rounded-full bg-blue-600 flex items-center justify-center text-4xl font-bold mx-auto">
            T
          </div>

          <h2 className="text-4xl font-bold text-center mt-6">
            Tanisha
          </h2>

          <p className="text-center text-gray-300 mt-3">
            B.Tech CSE Student
          </p>

          <div className="mt-8 space-y-4">
            <p>📍 Kurukshetra, Haryana</p>
            <p>📞 8571032055</p>
            <p>✉️ tanishac216@gmail.com</p>
          </div>

          <div className="mt-8">
            <h3 className="font-bold text-xl mb-3">Links</h3>

            <a
              href="https://www.linkedin.com/in/tanisha-chaudhary-121621292"
              target="_blank"
              className="block text-blue-400 underline"
            >
              LinkedIn
            </a>

            <a
              href="https://github.com/taniiishaa"
              target="_blank"
              className="block text-blue-400 underline"
            >
              GitHub
            </a>
          </div>
        </div>

        {/* Right Section */}
        <div className="flex-1 space-y-6">

          {/* Summary */}
          <div className="bg-white p-8 rounded-3xl shadow">
            <h2 className="text-3xl font-bold text-blue-700 mb-4">
              Professional Summary
            </h2>

            <p className="text-gray-700">
              Computer Science Engineering undergraduate with a strong
              interest in software development, cloud technologies, and
              artificial intelligence. Skilled in Python, C/C++, MySQL,
              HTML, CSS, and AWS fundamentals. Passionate about building
              practical solutions, participating in hackathons, and
              continuously learning new technologies to strengthen both
              technical and problem-solving abilities.
            </p>
          </div>

          {/* Skills */}
<div className="bg-white p-8 rounded-3xl shadow-lg">
  <h2 className="text-3xl font-bold text-blue-700 mb-4">
    Technical Skills
  </h2>

  <div className="flex flex-wrap gap-3">
    {skills.map((skill) => (
      <span
        key={skill}
        className="bg-blue-100 text-blue-900 border border-blue-300 font-medium px-4 py-2 rounded-full"
      >
        {skill}
      </span>
    ))}
  </div>
</div>

          {/* Education */}
<div className="bg-white p-8 rounded-3xl shadow-lg">
  <h2 className="text-3xl font-bold text-blue-700 mb-4">
    Education
  </h2>

  <div className="space-y-6 text-gray-800">

    <div>
      <h3 className="font-bold text-lg text-slate-900">
        B.Tech Computer Science Engineering
      </h3>
      <p className="text-gray-700">JMIT, Radaur</p>
      <p className="text-gray-600">2023 - 2027</p>
    </div>

    <div>
      <h3 className="font-bold text-lg text-slate-900">
        Class 12th
      </h3>
      <p className="text-gray-700">
        Wisdom World School, Kurukshetra
      </p>
    </div>

    <div>
      <h3 className="font-bold text-lg text-slate-900">
        Class 10th
      </h3>
      <p className="text-gray-700">
        Delhi Public School (DPS), Kurukshetra
      </p>
    </div>

  </div>
</div>

          {/* Projects Placeholder */}
          <div className="bg-white p-8 rounded-3xl shadow">
            <h2 className="text-3xl font-bold text-blue-700 mb-4">
              Projects
            </h2>

            <p className="text-gray-600">
              Projects will be added here.
            </p>
          </div>

        </div>
      </div>
    </div>
  );
}

export default AboutMe;