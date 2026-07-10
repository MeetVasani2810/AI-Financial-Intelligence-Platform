import { prisma } from "@repo/database/client";

async function main() {
  const time = new Date();

  // Create a new user
  const user = await prisma.testUser.create({
    data: {
      name: `${time.toLocaleString()}`,
      email: `${time.getTime()}@stockai.local`,
    },
  });
  console.log("Created user:", user);

  // Fetch all users
  const allUsers = await prisma.testUser.findMany();
  console.log("All users:", JSON.stringify(allUsers, null, 2));
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });