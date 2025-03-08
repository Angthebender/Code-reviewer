import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const { code } = await req.json();

    // Send the code to your Flask backend
    const response = await fetch("http://127.0.0.1:5000/optimize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    });

    const data = await response.json();
    
    return NextResponse.json({ optimized_code: data.optimized_code });
  } catch (error) {
    console.error("Error:", error); // Log the error to the console
    return NextResponse.json({ error: "Error processing code." }, { status: 500 });
  }
}
