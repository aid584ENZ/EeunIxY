import { withClerkMiddleware } from "@clerk/nextjs/server";

export default withClerkMiddleware((req) => {
  return NextResponse.next({
    request: req,
  });
});
