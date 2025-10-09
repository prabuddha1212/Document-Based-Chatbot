'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function Admin() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const [docId, setDocId] = useState('');
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
    }
  }, []);

  const handleUpload = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/documents/upload`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      });
      if (response.ok) {
        setMessage('Document uploaded successfully');
      } else {
        setMessage('Upload failed');
      }
    } catch (err) {
      setMessage('Upload failed');
    }
  };

  const handleDelete = async (docId) => {
    const token = localStorage.getItem('token');
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/documents/delete/${docId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      if (response.ok) {
        setMessage('Document deleted successfully');
      } else {
        setMessage('Delete failed');
      }
    } catch (err) {
      setMessage('Delete failed');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center mb-6">Admin Dashboard</h1>
        <form onSubmit={handleUpload} className="space-y-4">
          <div>
            <label htmlFor="file" className="block text-sm font-medium text-gray-700">
              Upload Document
            </label>
            <input
              id="file"
              name="file"
              type="file"
              required
              className="mt-1 block w-full"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </div>
          <button
            type="submit"
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Upload
          </button>
        </form>
        <div className="mt-6">
          <h2 className="text-lg font-medium mb-4">Delete Document</h2>
          <input
            type="text"
            placeholder="Document ID"
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            onChange={(e) => setDocId(e.target.value)}
          />
          <button
            onClick={() => handleDelete(docId)}
            className="mt-2 w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700"
          >
            Delete
          </button>
        </div>
        {message && <p className="mt-4 text-center text-sm text-gray-600">{message}</p>}
      </div>
    </div>
  );
}
