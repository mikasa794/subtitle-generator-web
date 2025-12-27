import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'open.feishu.cn',
      },
      {
        protocol: 'https',
        hostname: '*.feishucdn.com',
      },
    ],
  },
};

export default nextConfig;
