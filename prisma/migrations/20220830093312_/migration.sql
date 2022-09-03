-- CreateTable
CREATE TABLE "User" (
    "updated_at" TIMESTAMP(3),
    "sub" TEXT NOT NULL,
    "email" TEXT,
    "name" TEXT NOT NULL,
    "given_name" TEXT,
    "family_name" TEXT,
    "middle_name" TEXT,
    "nickname" TEXT,
    "preferred_username" TEXT,
    "profile" TEXT,
    "picture" TEXT,
    "website" TEXT,
    "gender" TEXT,
    "birthdate" TEXT,
    "zoneinfo" TEXT,
    "locale" TEXT,
    "phone_number" TEXT,
    "address" TEXT,
    "phone_number_verified" BOOLEAN,
    "email_verified" BOOLEAN,

    CONSTRAINT "User_pkey" PRIMARY KEY ("sub")
);

-- CreateTable
CREATE TABLE "Upload" (
    "id" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3),
    "filename" TEXT,
    "contentType" TEXT,
    "url" TEXT NOT NULL,
    "sub" TEXT NOT NULL,

    CONSTRAINT "Upload_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Profile" (
    "id" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3),
    "sub" TEXT NOT NULL,
    "skills" JSONB[],
    "jobs" JSONB[],
    "education" JSONB[],
    "theme" JSONB,
    "bio" TEXT,
    "location" TEXT,
    "email" TEXT,
    "name" TEXT,
    "picture" TEXT,

    CONSTRAINT "Profile_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Product" (
    "id" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3),
    "name" TEXT NOT NULL,
    "price" DOUBLE PRECISION NOT NULL,
    "description" TEXT,
    "quantity" INTEGER,
    "sub" TEXT NOT NULL,

    CONSTRAINT "Product_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Order" (
    "id" TEXT NOT NULL,
    "created_at" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3),
    "sub" TEXT NOT NULL,

    CONSTRAINT "Order_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "_OrderToProduct" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "User_sub_key" ON "User"("sub");

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE INDEX "User_email_sub_gender_idx" ON "User"("email", "sub", "gender");

-- CreateIndex
CREATE UNIQUE INDEX "Upload_url_key" ON "Upload"("url");

-- CreateIndex
CREATE INDEX "Upload_filename_sub_contentType_idx" ON "Upload"("filename", "sub", "contentType");

-- CreateIndex
CREATE UNIQUE INDEX "Profile_sub_key" ON "Profile"("sub");

-- CreateIndex
CREATE INDEX "Profile_sub_email_name_skills_jobs_education_location_idx" ON "Profile"("sub", "email", "name", "skills", "jobs", "education", "location");

-- CreateIndex
CREATE UNIQUE INDEX "Product_sub_key" ON "Product"("sub");

-- CreateIndex
CREATE UNIQUE INDEX "Order_sub_key" ON "Order"("sub");

-- CreateIndex
CREATE UNIQUE INDEX "_OrderToProduct_AB_unique" ON "_OrderToProduct"("A", "B");

-- CreateIndex
CREATE INDEX "_OrderToProduct_B_index" ON "_OrderToProduct"("B");

-- AddForeignKey
ALTER TABLE "Upload" ADD CONSTRAINT "Upload_sub_fkey" FOREIGN KEY ("sub") REFERENCES "User"("sub") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Upload" ADD CONSTRAINT "Upload_id_fkey" FOREIGN KEY ("id") REFERENCES "Product"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Profile" ADD CONSTRAINT "Profile_sub_fkey" FOREIGN KEY ("sub") REFERENCES "User"("sub") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Product" ADD CONSTRAINT "Product_sub_fkey" FOREIGN KEY ("sub") REFERENCES "User"("sub") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Order" ADD CONSTRAINT "Order_sub_fkey" FOREIGN KEY ("sub") REFERENCES "User"("sub") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_OrderToProduct" ADD CONSTRAINT "_OrderToProduct_A_fkey" FOREIGN KEY ("A") REFERENCES "Order"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_OrderToProduct" ADD CONSTRAINT "_OrderToProduct_B_fkey" FOREIGN KEY ("B") REFERENCES "Product"("id") ON DELETE CASCADE ON UPDATE CASCADE;
